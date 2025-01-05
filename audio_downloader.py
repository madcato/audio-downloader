import sys
import subprocess

def download_audio(url, output_file=None):
    try:
        # Construye el comando de yt-dlp
        command = ["yt-dlp", "-f", "bestaudio", "--extract-audio", "--audio-format", "mp3"]
        if output_file:
            command.extend(["-o", output_file])
        else:
            command.extend(["-o", "%(title)s.%(ext)s"])

        command.append(url)

        # Ejecuta el comando
        subprocess.run(command, check=True)
        print("Audio descargado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al descargar el audio: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python audio_downloader.py <URL> [nombre_archivo]")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    download_audio(url, output_file)
