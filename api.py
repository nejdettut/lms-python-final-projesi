def analyze_text(text):
return {
"kelime_sayisi": len(text.split()),
"ozet": text[:120] + "..."
}
