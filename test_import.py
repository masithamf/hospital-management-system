import requests
import json
from datetime import datetime

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkb2N0b3IiLCJleHAiOjE3NTg1Mjg5Mjl9.gJKxrauYXq3Qgsc0gSoAGJNMTOppxy4GY_ijrq5GvDY"

url = "http://127.0.0.1:8005/import"

# Data dummy untuk testing import
dummy_patients = [
    {
        "nama": "Alice",
        "tanggal_kunjungan": "2024-01-25T08:00:00"
    },
    {
        "nama": "Bob", 
        "tanggal_kunjungan": "2024-01-25T10:30:00",
        "diagnosis": "Flu",
        "tindakan": "Rest"
    },
    {
        "nama": "Charlie",
        "tanggal_lahir": "1985-03-15",
        "tanggal_kunjungan": "2024-01-25T14:00:00",
        "diagnosis": "Routine checkup",
        "tindakan": "Physical examination",
        "dokter": "Dr. External"
    },
    {
        "nama": "Diana",
        "tanggal_lahir": "1990-07-20",
        "tanggal_kunjungan": "2024-01-25T16:30:00",
        "diagnosis": "Migraine",
        "tindakan": "Pain relief and rest",
        "dokter": "Dr. External"
    },
    {
        "nama": "Edward",
        "tanggal_kunjungan": "2024-01-26T09:15:00"
    }
]

def test_import():
    """Function untuk test import data pasien"""
    
    print("=" * 50)
    print("HOSPITAL MANAGEMENT SYSTEM")
    print("Test Import External Data")
    print("=" * 50)
    
    # Validasi token
    if TOKEN == "YOUR_TOKEN_HERE" or len(TOKEN) < 50:
        print("ERROR: Token belum diganti atau tidak valid!")
        print("Token harus dimulai dengan 'eyJ' dan panjang minimal 50 karakter")
        input("\nTekan Enter untuk keluar...")
        return
    
    # Headers dengan token
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"access_token={TOKEN}"
    }
    
    print(f"Mengirim {len(dummy_patients)} data pasien ke server...")
    print(f"URL: {url}")
    print(f"Token: {TOKEN[:20]}...")
    print()
    
    try:
        # Kirim request
        response = requests.post(url, json=dummy_patients, headers=headers)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"BERHASIL!")
            print(f"{result['message']}")
            print(f"Jumlah diimport: {result['imported_count']} pasien")
            
            print("\nData yang diimport:")
            for i, patient in enumerate(dummy_patients, 1):
                print(f"  {i}. {patient['nama']} - {patient.get('tanggal_kunjungan', 'N/A')}")
                
        elif response.status_code == 303:
            print("BERHASIL!")
            print(f"Import berhasil! Server redirect ke halaman patients")
            print(f"Jumlah diimport: {len(dummy_patients)} pasien")
            
            print("\nData yang diimport:")
            for i, patient in enumerate(dummy_patients, 1):
                print(f"  {i}. {patient['nama']} - {patient.get('tanggal_kunjungan', 'N/A')}")
            
        elif response.status_code == 401:
            print("ERROR: Not authenticated")
            print("Token mungkin expired atau salah")
            print("Coba login ulang dan ambil token baru")
            
        else:
            print(f"ERROR: {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("ERROR: Tidak bisa connect ke server")
        print("Pastikan server berjalan di http://127.0.0.1:8005")
        
    except Exception as e:
        print(f"XCEPTION: {e}")
    
    print("\n" + "=" * 50)
    print("Cek hasil import di:")
    print("   Dashboard: http://127.0.0.1:8005/dashboard")
    print("   Patients:  http://127.0.0.1:8005/patients")
    print("=" * 50)

def test_dummy_endpoint():
    """Function untuk test endpoint dummy (tidak perlu token di header)"""
    
    print("\nTesting dummy endpoint...")
    
    headers = {
        "Cookie": f"access_token={TOKEN}"
    }
    
    try:
        response = requests.post("http://127.0.0.1:8005/import/dummy", headers=headers)
        
        if response.status_code == 303:
            print("Dummy import berhasil! (Redirect ke /patients)")
        else:
            print(f"Status: {response.status_code}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Test import JSON
    test_import()
    
    # Tanya user apakah mau test dummy juga
    print("\n" + "=" * 30)
    choice = input("Test dummy endpoint juga? (y/n): ").lower()
    if choice == 'y':
        test_dummy_endpoint()
    
    input("\nTekan Enter untuk keluar...")
