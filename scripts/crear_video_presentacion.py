from __future__ import annotations

import base64
import argparse
import asyncio
import json
import shutil
import subprocess
import sys
import wave
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "video_build_cloud"
OUTPUT = ROOT / "outputs" / "video_presentacion_titanic_5_minutos.mp4"
NOTEBOOK = ROOT / "notebooks" / "trabajo_titanic.ipynb"
VIDEO_TOOLS = ROOT / ".video_tools"

from PIL import Image, ImageDraw, ImageFont, ImageOps  # noqa: E402


WIDTH, HEIGHT = 1920, 1080
BLACK = "#171717"
WHITE = "#FFFFFF"
OFF_WHITE = "#F5F5F3"
YELLOW = "#F4C400"
GRAY = "#6C7077"
LIGHT_GRAY = "#E5E7EB"
GREEN = "#2E8B57"
BLUE = "#2457A6"

FONT_REGULAR = Path(r"C:\Windows\Fonts\segoeui.ttf")
FONT_BOLD = Path(r"C:\Windows\Fonts\segoeuib.ttf")
FONT_MONO = Path(r"C:\Windows\Fonts\consola.ttf")


SCENES = [
    {
        "slug": "01_portada",
        "title": "Portada",
        "speaker": "Cesar",
        "voice": "es-CL-LorenzoNeural",
        "text": (
            "Hola. Somos Javiera Retamal y Cesar Retamal. En este video presentamos "
            "nuestro trabajo de la Unidad 1 de Machine Learning de la Universidad Mayor, "
            "desarrollado con el conjunto de datos Titanic. El docente de la asignatura "
            "es Franco Andres Mansilla."
        ),
        "bullets": [
            "Machine Learning - Unidad 1",
            "Dataset: Titanic",
            "Javiera Retamal | Cesar Retamal",
            "Docente: Franco Andres Mansilla",
            "24-08-2026",
        ],
        "kind": "cover",
    },
    {
        "slug": "02_introduccion",
        "title": "Introducción",
        "speaker": "Javiera",
        "voice": "es-CL-CatalinaNeural",
        "text": (
            "El objetivo fue construir un pipeline reproducible para explorar, limpiar y "
            "separar los datos de pasajeros del Titanic, estudiando su relación con la "
            "supervivencia. El trabajo comprende la comparación de frameworks analíticos, "
            "la evaluación de la calidad de los datos, el tratamiento de valores faltantes "
            "y atípicos, y la creación de muestras de entrenamiento, validación y test sin "
            "fuga de información."
        ),
        "bullets": [
            "891 pasajeros",
            "12 variables",
            "Objetivo: Survived",
            "Pipeline reproducible",
            "Sin fuga de información",
        ],
        "kind": "cards",
    },
    {
        "slug": "03_punto_1",
        "title": "Punto 1. Frameworks analíticos",
        "speaker": "Cesar",
        "voice": "es-CL-LorenzoNeural",
        "text": (
            "Comparamos tres frameworks. CRISP D M organiza el proyecto en comprensión "
            "del negocio, comprensión de los datos, preparación, modelamiento, evaluación "
            "y despliegue. Su limitación es que entrega una guía general, pero no define "
            "herramientas concretas. K D D se enfoca en descubrir conocimiento mediante "
            "selección, transformación, minería e interpretación, aunque desarrolla menos "
            "el contexto del negocio y el despliegue. S E M M A considera muestreo, "
            "exploración, modificación, modelamiento y evaluación, pero tampoco incorpora "
            "formalmente la comprensión del negocio. Seleccionamos CRISP D M porque cubre "
            "el proyecto completo y permite volver a etapas anteriores cuando aparecen "
            "problemas en los datos."
        ),
        "bullets": [
            "CRISP-DM: proyecto completo e iterativo",
            "KDD: descubrimiento de conocimiento",
            "SEMMA: desarrollo técnico del modelo",
            "Selección: CRISP-DM",
        ],
        "kind": "frameworks",
    },
    {
        "slug": "04_punto_2",
        "title": "Punto 2. Calidad de los datos",
        "speaker": "Javiera",
        "voice": "es-CL-CatalinaNeural",
        "text": (
            "La base de desarrollo contiene 891 pasajeros y 12 variables. La variable "
            "objetivo es Survived, donde cero representa que el pasajero no sobrevivió y "
            "uno que sí sobrevivió. No encontramos filas completamente duplicadas. Los "
            "principales problemas de calidad fueron los valores faltantes en Age, Cabin "
            "y Embarked, además de valores elevados en Fare y en algunos recuentos "
            "familiares. Para Age y Fare usamos imputación por mediana, y para Embarked, "
            "imputación por moda. Como Cabin tiene una ausencia muy alta, no inventamos "
            "una cabina; creamos las variables Has Cabin y Deck. Los valores altos de Fare "
            "pueden ser pasajes legítimos de primera clase, por lo que aplicamos una "
            "transformación logarítmica en vez de eliminarlos. También creamos Family Size, "
            "Is Alone y Title. Todas las estadísticas de imputación y escalamiento se "
            "aprenden solamente con los datos de entrenamiento para evitar fuga de información."
        ),
        "bullets": [
            "Age y Fare: mediana",
            "Embarked: moda",
            "Cabin: HasCabin + Deck",
            "Fare: transformación log1p",
            "0 filas duplicadas",
        ],
        "kind": "quality",
    },
    {
        "slug": "05_punto_3",
        "title": "Punto 3. Entrenamiento, validación y test",
        "speaker": "Cesar",
        "voice": "es-CL-LorenzoNeural",
        "text": (
            "Evaluamos tres alternativas. La división aleatoria simple es rápida, pero "
            "puede alterar la proporción de supervivientes. La división estratificada "
            "conserva esa proporción en cada muestra. La validación cruzada estratificada "
            "entrega una evaluación más estable, aunque requiere mayor procesamiento y no "
            "sustituye un test final independiente. Seleccionamos una división aleatoria "
            "estratificada de 70 por ciento para entrenamiento, 15 por ciento para "
            "validación y 15 por ciento para test, usando random state igual a 42. Así "
            "obtuvimos 623, 134 y 134 observaciones, respectivamente. Implementamos un "
            "pipeline con preprocesamiento y regresión logística. La exactitud fue 0 coma "
            "8881 en validación y 0 coma 7910 en el test interno final. Además, la balanced "
            "accuracy promedio de la validación cruzada de cinco particiones fue 0 coma "
            "8096. La diferencia entre validación y test confirma la importancia de no "
            "depender de una sola partición."
        ),
        "bullets": [
            "Train: 623 (70%)",
            "Validación: 134 (15%)",
            "Test interno: 134 (15%)",
            "Accuracy validación: 0,8881",
            "Accuracy test: 0,7910",
            "Balanced accuracy CV: 0,8096",
        ],
        "kind": "metrics",
    },
    {
        "slug": "06_punto_4",
        "title": "Punto 4. Repositorio de GitHub",
        "speaker": "Javiera",
        "voice": "es-CL-CatalinaNeural",
        "text": (
            "Todo el desarrollo se guardó en un repositorio público de GitHub. Incluye los "
            "datos originales, el cuaderno ejecutado, el archivo de predicciones, las "
            "dependencias y un README con instrucciones de reproducción. El código usa "
            "rutas relativas y mantiene el preprocesamiento unido al modelo mediante un pipeline."
        ),
        "bullets": [
            "data/ - archivos originales",
            "notebooks/ - trabajo_titanic.ipynb",
            "outputs/ - predicciones y video",
            "README.md - ejecución y resultados",
            "requirements.txt - dependencias",
        ],
        "kind": "github",
    },
    {
        "slug": "07_conclusion",
        "title": "Conclusión",
        "speaker": "Cesar y Javiera",
        "voice": "es-CL-LorenzoNeural",
        "text": (
            "En conclusión, la calidad de los datos y una separación correcta son "
            "fundamentales para obtener resultados confiables. CRISP D M permitió organizar "
            "el trabajo de forma iterativa, mientras que el pipeline evitó fugas de "
            "información y facilitó la reproducibilidad. El modelo base obtuvo resultados "
            "razonables, pero el principal resultado es un proceso documentado, repetible "
            "y preparado para futuras mejoras. Muchas gracias."
        ),
        "bullets": [
            "Calidad antes de modelar",
            "Separación estratificada y reproducible",
            "Pipeline sin fuga de información",
            "Proceso documentado y mejorable",
        ],
        "kind": "conclusion",
    },
]


def font(size: int, bold: bool = False, mono: bool = False) -> ImageFont.FreeTypeFont:
    path = FONT_MONO if mono else (FONT_BOLD if bold else FONT_REGULAR)
    return ImageFont.truetype(str(path), size)


def wrap_text(draw: ImageDraw.ImageDraw, text: str, face, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if draw.textbbox((0, 0), candidate, font=face)[2] <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def rounded_box(draw, xy, fill, outline=None, radius=24, width=2):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def draw_header(draw: ImageDraw.ImageDraw, title: str, speaker: str, index: int):
    draw.rectangle((0, 0, WIDTH, 150), fill=BLACK)
    draw.rectangle((0, 142, WIDTH, 150), fill=YELLOW)
    draw.text((80, 43), title, font=font(51, bold=True), fill=WHITE)
    badge = f"VOZ: {speaker.upper()}"
    badge_face = font(24, bold=True)
    badge_width = draw.textbbox((0, 0), badge, font=badge_face)[2] + 48
    rounded_box(draw, (WIDTH - badge_width - 80, 48, WIDTH - 80, 105), YELLOW, radius=18)
    draw.text((WIDTH - badge_width - 56, 61), badge, font=badge_face, fill=BLACK)
    draw.text((80, HEIGHT - 60), "Universidad Mayor | Machine Learning | Titanic", font=font(23), fill=GRAY)
    draw.text((WIDTH - 155, HEIGHT - 60), f"{index}/7", font=font(23, bold=True), fill=GRAY)
    draw.rectangle((0, HEIGHT - 12, int(WIDTH * index / 7), HEIGHT), fill=YELLOW)


def draw_bullets(draw, bullets, x, y, width, size=34, gap=18):
    face = font(size)
    y_pos = y
    for item in bullets:
        lines = wrap_text(draw, item, face, width - 60)
        draw.ellipse((x, y_pos + 13, x + 16, y_pos + 29), fill=YELLOW)
        for line_no, line in enumerate(lines):
            draw.text((x + 38, y_pos + line_no * (size + 9)), line, font=face, fill=BLACK)
        y_pos += len(lines) * (size + 9) + gap


def extract_notebook_plots() -> dict[int, Path]:
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    wanted = {11, 13, 26}
    paths: dict[int, Path] = {}
    for idx, cell in enumerate(notebook["cells"]):
        if idx not in wanted:
            continue
        for output in cell.get("outputs", []):
            data = output.get("data", {}).get("image/png")
            if data:
                encoded = "".join(data) if isinstance(data, list) else data
                path = BUILD / f"notebook_plot_{idx}.png"
                path.write_bytes(base64.b64decode(encoded))
                paths[idx] = path
                break
    return paths


def paste_contained(canvas: Image.Image, source_path: Path, box: tuple[int, int, int, int]):
    source = Image.open(source_path).convert("RGB")
    target_w, target_h = box[2] - box[0], box[3] - box[1]
    contained = ImageOps.contain(source, (target_w, target_h), Image.Resampling.LANCZOS)
    x = box[0] + (target_w - contained.width) // 2
    y = box[1] + (target_h - contained.height) // 2
    canvas.paste(contained, (x, y))


def make_slide(scene: dict, index: int, plots: dict[int, Path]) -> Path:
    canvas = Image.new("RGB", (WIDTH, HEIGHT), OFF_WHITE)
    draw = ImageDraw.Draw(canvas)
    draw_header(draw, scene["title"], scene["speaker"], index)
    kind = scene["kind"]

    if kind == "cover":
        draw.text((110, 250), "TRABAJO UNIDAD 1", font=font(36, bold=True), fill=YELLOW)
        draw.text((110, 310), "Machine Learning", font=font(92, bold=True), fill=BLACK)
        draw.text((110, 425), "Análisis reproducible del dataset Titanic", font=font(43), fill=GRAY)
        draw.rectangle((110, 510, 1810, 516), fill=YELLOW)
        draw_bullets(draw, scene["bullets"][2:], 130, 570, 1500, size=38, gap=20)
        rounded_box(draw, (1410, 260, 1760, 440), BLACK, radius=36)
        draw.text((1478, 292), "891", font=font(74, bold=True), fill=YELLOW)
        draw.text((1458, 382), "pasajeros", font=font(30), fill=WHITE)

    elif kind == "cards":
        labels = [
            ("891", "pasajeros"), ("12", "variables"), ("Survived", "objetivo"),
            ("70/15/15", "split"), ("42", "semilla"),
        ]
        positions = [(100, 240), (700, 240), (1300, 240), (390, 570), (1030, 570)]
        for (value, label), (x, y) in zip(labels, positions):
            rounded_box(draw, (x, y, x + 500, y + 240), WHITE, LIGHT_GRAY, radius=28, width=3)
            draw.text((x + 34, y + 38), value, font=font(62, bold=True), fill=BLACK)
            draw.text((x + 34, y + 137), label.upper(), font=font(28, bold=True), fill=BLUE)

    elif kind == "frameworks":
        columns = [
            ("CRISP-DM", "Negocio → Datos → Preparación → Modelo → Evaluación → Despliegue", True),
            ("KDD", "Selección → Preproceso → Transformación → Minería → Interpretación", False),
            ("SEMMA", "Muestrear → Explorar → Modificar → Modelar → Evaluar", False),
        ]
        for i, (name, desc, selected) in enumerate(columns):
            x = 90 + i * 610
            fill = "#FFF8D6" if selected else WHITE
            outline = YELLOW if selected else LIGHT_GRAY
            rounded_box(draw, (x, 240, x + 550, 800), fill, outline, radius=30, width=5 if selected else 3)
            draw.text((x + 35, 285), name, font=font(46, bold=True), fill=BLACK)
            lines = wrap_text(draw, desc, font(31), 470)
            for j, line in enumerate(lines):
                draw.text((x + 35, 390 + j * 51), line, font=font(31), fill=GRAY)
            if selected:
                rounded_box(draw, (x + 35, 690, x + 310, 755), YELLOW, radius=18)
                draw.text((x + 61, 704), "SELECCIONADO", font=font(26, bold=True), fill=BLACK)

    elif kind == "quality":
        rounded_box(draw, (70, 205, 1240, 900), WHITE, LIGHT_GRAY, radius=28)
        if 11 in plots:
            paste_contained(canvas, plots[11], (105, 235, 1205, 560))
        if 13 in plots:
            paste_contained(canvas, plots[13], (105, 575, 1205, 865))
        rounded_box(draw, (1280, 205, 1845, 900), "#FFF8D6", YELLOW, radius=28, width=3)
        draw.text((1330, 250), "Tratamientos", font=font(39, bold=True), fill=BLACK)
        draw_bullets(draw, scene["bullets"], 1330, 335, 455, size=30, gap=22)

    elif kind == "metrics":
        rounded_box(draw, (70, 210, 1000, 900), WHITE, LIGHT_GRAY, radius=28)
        if 26 in plots:
            paste_contained(canvas, plots[26], (100, 245, 970, 865))
        rounded_box(draw, (1040, 210, 1850, 900), "#F3F7FC", "#B9C9DF", radius=28, width=3)
        draw.text((1090, 255), "Split estratificado", font=font(40, bold=True), fill=BLACK)
        draw_bullets(draw, scene["bullets"], 1090, 340, 700, size=31, gap=17)

    elif kind == "github":
        rounded_box(draw, (100, 220, 1820, 880), WHITE, LIGHT_GRAY, radius=28)
        draw.text((150, 265), "CesarRR33 / TRABAJOS-MACHINE-LEARNING-UMAYOR", font=font(40, bold=True), fill=BLACK)
        rounded_box(draw, (150, 335, 1770, 740), "#0D1117", radius=18)
        tree = [
            ("📁  data/", YELLOW),
            ("📁  notebooks/", YELLOW),
            ("📁  outputs/", YELLOW),
            ("📄  README.md", WHITE),
            ("📄  requirements.txt", WHITE),
        ]
        for i, (label, color) in enumerate(tree):
            safe_label = label.replace("📁", "+").replace("📄", "-")
            draw.text((205, 380 + i * 62), safe_label, font=font(31, mono=True), fill=color)
        draw.text((150, 785), "github.com/CesarRR33/TRABAJOS-MACHINE-LEARNING-UMAYOR", font=font(31), fill=BLUE)

    elif kind == "conclusion":
        points = [
            ("1", "Calidad de datos", "Imputación y tratamiento con criterios reproducibles."),
            ("2", "Evaluación confiable", "Split estratificado, validación cruzada y test final."),
            ("3", "Pipeline reproducible", "Preprocesamiento y modelo unidos, documentados en GitHub."),
        ]
        for i, (number, title, desc) in enumerate(points):
            x = 100 + i * 600
            rounded_box(draw, (x, 245, x + 535, 790), WHITE, LIGHT_GRAY, radius=30)
            rounded_box(draw, (x + 35, 290, x + 125, 380), YELLOW, radius=25)
            draw.text((x + 65, 302), number, font=font(46, bold=True), fill=BLACK)
            draw.text((x + 35, 435), title, font=font(38, bold=True), fill=BLACK)
            lines = wrap_text(draw, desc, font(30), 455)
            for j, line in enumerate(lines):
                draw.text((x + 35, 515 + j * 48), line, font=font(30), fill=GRAY)
        draw.text((100, 860), "Proceso documentado, repetible y preparado para futuras mejoras.", font=font(36, bold=True), fill=BLUE)

    path = BUILD / f"{scene['slug']}.png"
    canvas.save(path, quality=95)
    return path


def synthesize_audio(scene: dict) -> tuple[Path, float]:
    text_path = BUILD / f"{scene['slug']}.txt"
    mp3_path = BUILD / f"{scene['slug']}.mp3"
    audio_path = BUILD / f"{scene['slug']}.wav"
    text_path.write_text(scene["text"], encoding="utf-8")
    sys.path.insert(0, str(VIDEO_TOOLS))
    import edge_tts
    asyncio.run(edge_tts.Communicate(scene["text"], scene["voice"], rate="-5%").save(str(mp3_path)))
    run_ffmpeg(["-i", str(mp3_path), "-ar", "24000", "-ac", "1", str(audio_path)])
    with wave.open(str(audio_path), "rb") as wav:
        duration = wav.getnframes() / wav.getframerate()
    return audio_path, duration


def run_ffmpeg(args: list[str]):
    sys.path.insert(0, str(VIDEO_TOOLS))
    import imageio_ffmpeg
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    subprocess.run([ffmpeg, "-hide_banner", "-loglevel", "error", "-y", *args], check=True)


def make_video_segment(slide: Path, audio: Path, duration: float, slug: str) -> Path:
    segment = BUILD / f"{slug}.mp4"
    total = duration + 0.65
    run_ffmpeg([
        "-loop", "1", "-framerate", "30", "-i", str(slide), "-i", str(audio),
        "-vf", "scale=1920:1080,format=yuv420p",
        "-af", "apad=pad_dur=0.65",
        "-t", f"{total:.3f}", "-c:v", "libx264", "-preset", "medium",
        "-tune", "stillimage", "-r", "30", "-c:a", "aac", "-b:a", "160k",
        "-movflags", "+faststart", str(segment),
    ])
    return segment


def create_contact_sheet(slides: list[Path]):
    thumb_w, thumb_h = 480, 270
    sheet = Image.new("RGB", (thumb_w * 2, thumb_h * 4), "#D4D4D4")
    for idx, slide in enumerate(slides):
        thumb = Image.open(slide).convert("RGB").resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        sheet.paste(thumb, ((idx % 2) * thumb_w, (idx // 2) * thumb_h))
    sheet.save(BUILD / "contact_sheet.png")


def build_assets():
    if BUILD.exists():
        shutil.rmtree(BUILD)
    BUILD.mkdir(parents=True)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    plots = extract_notebook_plots()
    slides: list[Path] = []
    durations: list[float] = []

    for index, scene in enumerate(SCENES, start=1):
        slide = make_slide(scene, index, plots)
        _, duration = synthesize_audio(scene)
        slides.append(slide)
        durations.append(duration + 0.65)

    create_contact_sheet(slides)
    (BUILD / "durations.json").write_text(json.dumps(durations), encoding="utf-8")
    print(json.dumps({"assets": len(slides), "duration_seconds": round(sum(durations), 2)}, ensure_ascii=False))


def encode_video():
    durations = json.loads((BUILD / "durations.json").read_text(encoding="utf-8"))
    segments: list[Path] = []
    for scene, total_duration in zip(SCENES, durations):
        slide = BUILD / f"{scene['slug']}.png"
        audio = BUILD / f"{scene['slug']}.wav"
        segment = make_video_segment(slide, audio, float(total_duration) - 0.65, scene["slug"])
        segments.append(segment)

    concat_file = BUILD / "concat.txt"
    concat_file.write_text(
        "\n".join(f"file '{segment.as_posix()}'" for segment in segments),
        encoding="utf-8",
    )
    run_ffmpeg([
        "-f", "concat", "-safe", "0", "-i", str(concat_file),
        "-c", "copy", "-movflags", "+faststart", str(OUTPUT),
    ])
    summary = {
        "output": str(OUTPUT),
        "duration_seconds": round(sum(durations), 2),
        "duration_mm_ss": f"{int(sum(durations) // 60)}:{int(sum(durations) % 60):02d}",
        "scenes": len(SCENES),
        "voices": sorted({scene["voice"] for scene in SCENES}),
    }
    (BUILD / "resumen.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--assets-only", action="store_true")
    parser.add_argument("--encode-only", action="store_true")
    args = parser.parse_args()
    if args.assets_only and args.encode_only:
        parser.error("Seleccione solo una etapa")
    if args.assets_only:
        build_assets()
    elif args.encode_only:
        encode_video()
    else:
        build_assets()
        encode_video()


if __name__ == "__main__":
    main()
