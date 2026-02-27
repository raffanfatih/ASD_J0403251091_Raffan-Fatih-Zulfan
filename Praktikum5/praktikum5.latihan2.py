# ==========================================================
# Latihan 2: Tracing Rekursi
# ==========================================================

def countdown(n):
    # fungsi if ini diperlukan karena tanpa kondisi ini fingsi akan terus berjalan tanpa ada batasan tertentu
    if n == 0:
        print("Selesai") 
        return
    print("Masuk:", n)
    countdown(n - 1) # fungsi memanggil dirinya sendiri dengan nilai n yang dikurangi 1 (n-1) sampai nilainya 0 (if n == 0)
    print("Keluar:", n) # fungsi ini akan muncul jika fungsi countdown(n-1) telah selesai, namun nilainya akan mulai dari 1 karena nilai yang terakhir disimpan akan muncul pertama
    
countdown(3)