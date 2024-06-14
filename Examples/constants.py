# test_files.py
# This module defines paths to test files.

import os
from os.path import join
import platform
import inspect


license_path = ""
input_path = "./Resources/SampleFiles/"
fonts_path = "./Resources/Fonts"
output_path = "./Output/"

def get_input_file_path(file_path):
    if platform.system() == 'Windows':
        return join(input_path, file_path)
    else:
        entry_dir = os.path.dirname(__file__)
        return join(entry_dir, input_path, file_path)

def get_output_file_path(file_path):
    if platform.system() == 'Windows':
        return join(output_path, file_path)
    else:
        entry_dir = os.path.dirname(__file__)
        return join(entry_dir, output_path, file_path)

input_docx = get_input_file_path("input.docx")
input_pptx = get_input_file_path("input.pptx")
input_xlsx = get_input_file_path("input.xlsx")
input_vsdx = get_input_file_path("input.vsdx")
input_vdx = get_input_file_path("input.vdx")
input_pdf = get_input_file_path("input.pdf")
input_one = get_input_file_path("input.one")
input_doc = get_input_file_path("input.doc")
input_ppt = get_input_file_path("input.ppt")
input_xls = get_input_file_path("input.xls")
input_jpeg = get_input_file_path("input.jpg")
input_png = get_input_file_path("input.png")
input_gif = get_input_file_path("input.gif")
input_dng = get_input_file_path("sample1.dng")
input_mpp = get_input_file_path("input.mpp")
input_bmp = get_input_file_path("input.bmp")
input_jpeg2000 = get_input_file_path("input.jp2")
input_dicom = get_input_file_path("input.dicom")
input_asf = get_input_file_path("input.asf")
input_avi = get_input_file_path("input.avi")
input_flv = get_input_file_path("input.flv")
input_mkv = get_input_file_path("input.mkv")
input_mov = get_input_file_path("input.mov")
input_wav = get_input_file_path("input.wav")
input_zip = get_input_file_path("input.zip")
input_rar = get_input_file_path("input.rar")
input_tar = get_input_file_path("input.tar")
input_seven_zip = get_input_file_path("input.7z")
input_vcf = get_input_file_path("input.vcf")
input_dxf = get_input_file_path("input.dxf")
input_epub = get_input_file_path("input.epub")
input_eml = get_input_file_path("input.eml")
input_msg = get_input_file_path("input.msg")
input_ttf = get_input_file_path("input.ttf")
input_torrent = get_input_file_path("input.torrent")
png_with_xmp = get_input_file_path("xmp.png")
gif_with_xmp = get_input_file_path("xmp.gif")
jpeg_with_xmp = get_input_file_path("xmp.jpg")
tiff_with_exif = get_input_file_path("exif.tiff")
tiff_with_iptc = get_input_file_path("iptc.tiff")
jpeg_with_exif = get_input_file_path("exif.jpg")
jpeg_with_iptc = get_input_file_path("iptc.jpg")
psd_with_iptc = get_input_file_path("iptc.psd")
psd_with_exif = get_input_file_path("exif.psd")
jpeg_with_irb = get_input_file_path("irb.jpg")
jpeg_with_barcodes = get_input_file_path("barcode.jpg")
psd_with_irb = get_input_file_path("irb.psd")
protected_docx = get_input_file_path("protected.docx")
signed_pdf = get_input_file_path("signed.pdf")
mkv_with_subtitles = get_input_file_path("subtitles.mkv")
mp3_with_ID3V1 = get_input_file_path("id3v1.mp3")
mp3_with_ID3V2 = get_input_file_path("id3v2.mp3")
mp3_with_Lyrics = get_input_file_path("lyrics.mp3")
mp3_with_Ape = get_input_file_path("ape.mp3")
canon_jpeg = get_input_file_path("canon_raw.jpg")
nikon_jpeg = get_input_file_path("nikon_raw.jpg")
panasonic_jpeg = get_input_file_path("panasonic_raw.jpg")
sony_jpeg = get_input_file_path("sony_raw.jpg")
input_Cr2 = get_input_file_path("input.CR2")

input_3ds = get_input_file_path("input.3ds")
input_Dae = get_input_file_path("input.dae")
input_Fbx = get_input_file_path("input.fbx")
input_Stl = get_input_file_path("input.stl")


output_docx = get_output_file_path("output.docx")
output_pptx = get_output_file_path("output.pptx")
output_xlsx = get_output_file_path("output.xlsx")
output_vsdx = get_output_file_path("output.vsdx")
output_vdx = get_output_file_path("output.vdx")
output_pdf = get_output_file_path("output.pdf")
output_one = get_output_file_path("output.one")
output_doc = get_output_file_path("output.doc")
output_ppt = get_output_file_path("output.ppt")
output_xls = get_output_file_path("output.xls")
output_mpp = get_output_file_path("output.mpp")
output_jpeg = get_output_file_path("output.jpg")
output_png = get_output_file_path("output.png")
output_gif = get_output_file_path("output.gif")
output_tiff = get_output_file_path("output.tiff")
output_psd = get_output_file_path("output.psd")
output_bmp = get_output_file_path("output.bmp")
output_mp3 = get_output_file_path("output.mp3")
output_zip = get_output_file_path("output.zip")
output_eml = get_output_file_path("output.eml")
output_torrent = get_output_file_path("output.torrent")
output_csv = get_output_file_path("output.csv")
output_epub = get_output_file_path("output.epub")
output_dxf = get_output_file_path("output.dxf")
output_xml = get_output_file_path("output.xml")