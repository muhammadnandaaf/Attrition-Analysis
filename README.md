# **Proyek Pertama: Menyelesaikan Permasalahan Human Resource**

## **Business Understanding**

### **Latar Belakang Bisnis**

Jaya Jaya Maju adalah perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1000 karyawan yang tersebar di berbagai wilayah di Indonesia. Seiring pertumbuhan perusahaan yang pesat, pengelolaan sumber daya manusia menjadi semakin kompleks dan menantang. Salah satu isu kritis yang dihadapi saat ini adalah tingginya tingkat attrition, yaitu rasio karyawan yang keluar dibandingkan dengan total jumlah karyawan.

Meskipun perusahaan telah berkembang menjadi organisasi besar, angka attrition yang melebihi 10% menunjukkan adanya permasalahan mendasar yang perlu segera diatasi. Tingginya tingkat perputaran karyawan tidak hanya berdampak pada biaya rekrutmen dan pelatihan, tetapi juga dapat menurunkan produktivitas serta semangat kerja tim yang tersisa.

Departemen Human Resources (HR) menyadari bahwa pendekatan konvensional dalam mengelola karyawan sudah tidak lagi efektif. Oleh karena itu, diperlukan pendekatan berbasis data untuk memahami secara mendalam faktor-faktor apa saja yang memengaruhi keputusan karyawan untuk meninggalkan perusahaan. Melalui proyek ini, dilakukan analisis menyeluruh terhadap data karyawan yang tersedia untuk mengidentifikasi pola, tren, dan faktor utama yang berkontribusi terhadap attrition. Selain itu, dibangun pula sebuah model prediktif yang dapat membantu memetakan risiko keluarnya karyawan di masa depan. Hasil analisis ini kemudian divisualisasikan dalam bentuk dashboard interaktif yang dapat digunakan oleh manajemen HR sebagai alat bantu pengambilan keputusan.

Dengan adanya pendekatan ini, perusahaan diharapkan dapat merumuskan strategi yang lebih efektif untuk meningkatkan retensi karyawan, menciptakan lingkungan kerja yang lebih sehat dan mendukung, serta pada akhirnya meningkatkan kinerja dan daya saing perusahaan secara keseluruhan.

### **Permasalahan Bisnis**

Masalah-masalah bisnis yang melatarbelakangi proyek ini antara lain:
1. Tingginya angka attrition: Tingkat karyawan yang keluar mencapai lebih dari 10%, yang jauh di atas ambang normal. Hal ini menjadi sinyal adanya ketidakpuasan atau ketidakcocokan dalam lingkungan kerja perusahaan.
2. Minimnya pemahaman atas penyebab attrition: Hingga saat ini, perusahaan belum memiliki pemahaman menyeluruh mengenai faktor-faktor apa saja yang paling berpengaruh terhadap keputusan karyawan untuk keluar.
3. Dampak terhadap produktivitas dan biaya operasional: Tingginya angka pergantian karyawan menimbulkan beban biaya rekrutmen dan pelatihan ulang, serta berpotensi menurunkan produktivitas karena hilangnya pengalaman kerja yang sudah terakumulasi.
4. Kebutuhan akan pengambilan keputusan berbasis dashboard: Manajemen HR membutuhkan alat bantu visual seperti dashboard untuk memantau faktor-faktor yang memengaruhi retensi karyawan secara real-time dan informatif.

### **Cakupan Proyek**

Proyek ini mencakup:
1. Eksplorasi dan Pembersihan Data
    - Menggunakan dataset `employee_data.csv` yang berisi informasi karyawan seperti usia, jenis kelamin, divisi, status pernikahan, gaji, dan status attrition.
    - Melakukan pengecekan missing values, duplikasi, dan konsistensi data.
    - Mengubah tipe data yang sesuai (misalnya pada kolom kategori), serta encoding pada variabel kategorikal.
2. Analisis Eksploratori (Exploratory Data Analysis / EDA)
    - Visualisasi distribusi berbagai variabel (usia, divisi, jenjang pendidikan, dll).
    - Analisis hubungan antara fitur-fitur tertentu terhadap attrition, misalnya:
        - Apakah karyawan dari divisi tertentu lebih banyak keluar?
        - Apakah tingkat gaji berpengaruh terhadap tingkat attrition?
        - Apakah usia atau status pernikahan memengaruhi keputusan keluar?
3. Identifikasi Faktor-Faktor Penyebab Tingginya Attrition
    - Menggunakan visualisasi seperti countplot, boxplot, dan heatmap untuk memahami korelasi dan pola antara variabel-variabel terhadap attrition.
    - Menyimpulkan fitur-fitur mana yang tampak berkontribusi besar terhadap keluarnya karyawan, seperti:
        - Gaji rendah
        - Divisi tertentu (seperti Sales)
        - Status pernikahan tertentu
4. Pembuatan Dashboard Interaktif
    - Menyiapkan data untuk digunakan dalam visualisasi dashboard
    - Memungkinkan manajemen HR untuk mengambil keputusan berbasis data.
5. Penyusunan Insight dan Rekomendasi
    - Memberikan insight berdasarkan hasil analisis, seperti:
        - Fokus pada retensi karyawan di divisi dengan tingkat keluar tinggi.
        - Peninjauan ulang kebijakan kompensasi dan tunjangan.
        - Pengembangan strategi kesejahteraan dan loyalitas karyawan.


### **Persiapan**

**Sumber Data:** 

Dataset yang digunakan dalam proyek ini adalah Dataset [Karyawan Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv) sesuai dengan instruksi dari submission proyek ini.

**Setup Environtment:**

Proyek ini memerlukan lingkungan kerja yang sederhana untuk melakukan analisis data serta membangun dashboard. Berikut ini merupakan tahapan-tahapan dalam menyiapkan environment tersebut:
1. Setup `notebook.ipynb`
- Download proyek ini terlebih dahulu.
- Pastikan dependensi, packages, library yang dibutuhkan sudah tersedia (lihat file requirements.txt untuk melihat dependensi yang dibutuhkan).
- Buka menggunakan VSCode Jupyter Notebook atau Google Colaboratory.
    * Menggunakan Jupyter Notebook 
        - Buka Terminal
        - Arahkan ke direktori tempat file proyek disimpan.
        - Contoh: `cd D:this/file/to/your/path`
        - Jalankan perintah `jupyter lab .` / `jupyter notebook`
    * Menggunakan Google Colaboratory
        - Buka Notebook baru
        - Upload dan pilih file ini (notebook.ipynb)
        - Sambungkan ke runtime yang disediakan Google.
        - Kemudian jalankan seluruh sel kode.
2. Setup Dashboard
- Gunakan metabase dengan docker
    - Buka terminal/wsl
    - Jalankan perintah berikut:
    ```
    docker pull metabase/metabase:v0.46.4
    ```
    - Jalankan container metabase:
    ```
    docker run -p 3000:3000 --name metabase metabase/metabase
    ```
    - Login ke metabase dengan username dan password:
    ```
    username: root@mail.com
    password: root123
    ```

## **Business Dashboard**

Hasil analisis dan model prediktif dapat disajikan dalam bentuk dashboard untuk membantu tim HR dalam memantau serta memahami tingkat attrition. Analisis yang disertakan dalam dashboard:
1. Ringkasan Statistik (Overview)

    Elemen-elemen ini memberikan gambaran umum terkait jumlah dan proporsi karyawan yang keluar: 
    - Total Karyawan
    - Total Karyawan Keluar        
    - Persentase Karyawan Keluar

2. Analisis Demografis & Karakteristik Personal
    
    Elemen-elemen ini menunjukkan profil karyawan yang keluar berdasarkan demografi:
    - Distribusi Usia Karyawan yang Keluar
    - Analisis Attrition Berdasarkan Gender
    - Hubungan antara Status Pernikahan dan Pendapatan Karyawan

3. Analisis Berdasarkan Pekerjaan & Departemen

    Elemen-elemen ini mengevaluasi attrition berdasarkan divisi dan peran::
    - Distribusi Tingkat Attrition Berdasarkan Job Role
    - Perbandingan Tingkat Attrition antar Departemen
    - Distribusi Attrition (berdasarkan jenis pekerjaan)
    - Rincian Attrition Karyawan Lembur

4. Analisis Faktor Penyebab Attrition

    Visualisasi yang menunjukkan variabel-variabel yang paling berpengaruh terhadap keluarnya karyawan:
    - Feature Importance (Nilai kontribusi tiap fitur terhadap attrition)
    - Attrition Factor Analysis (Hubungan antar kepuasan kerja, gaji, masa kerja, dll)

5. Analisis Berdasarkan Lama Bekerja dan Gaji

    Elemen yang berfokus pada hubungan antara masa kerja, pendapatan, dan tingkat attrition:
    - Tren Total Karyawan Keluar Berdasarkan Masa Kerja
    - Distribusi Karyawan Lembur dan Pendapatan Per Bulan

### **Cara Mengakses Dashboard**
1. Buka Docker Desktop yang telah disiapkan pada tahap Setup Environment.
2. Jalankan dan buka container yang terdapat di dalam Docker.
3. Salin link port localhost dari container dengan nama `metabase`.
4. Buka aplikasi Metabase melalui browser menggunakan link tersebut.
5. Masukkan username dan password untuk login ke Metabase.
    ```
    username: root@mail.com 
    password: root123
    ```

## **Conclusion**

Proyek analisis data terkait tingkat attrition karyawan di perusahaan **Jaya Jaya Maju** bertujuan utama untuk mendukung manajemen—khususnya tim HR (Human Resources)—dalam memahami faktor-faktor kunci yang menyebabkan tingginya angka karyawan keluar masuk (attrition).

🎯 **Tujuan Proyek Ini**:
- Menemukan faktor-faktor utama penyebab karyawan keluar dari perusahaan
- Membangun model prediktif untuk mengidentifikasi karyawan yang berisiko tinggi keluar
- Menyediakan dasar pengambilan keputusan yang didorong oleh data bagi pihak manajemen
- Mengembangkan dashboard interaktif sebagai alat bantu pemantauan
- Mengurangi dampak negatif serta biaya yang ditimbulkan oleh tingginya attrition rate

📊 **Evaluasi Akhir Model Random Forrest**:
- Model sangat baik dalam mengenali karyawan yang tidak keluar (kelas 0), dengan recall 97.7%.
- Namun, masih perlu ditingkatkan dalam mengenali karyawan yang keluar (kelas 1), karena recall-nya hanya 35.9%.
- Hal ini menunjukkan bahwa model cenderung bias ke kelas mayoritas (tidak keluar), meskipun presisinya cukup tinggi.

<table border="1">
  <thead>
    <tr>
      <th>Metode</th>
      <th>Akurasi</th>
      <th>Presisi</th>
      <th>Recall</th>
      <th>F1-Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Random Forest (BayesOpt)</td>
      <td>0.863208</td>
      <td>0.824456</td>
      <td>0.667926</td>
      <td>0.706104</td>
    </tr>
  </tbody>
</table>

<h3>Classification Report (BayesOpt Random Forest)</h3>

<table border="1">
  <thead>
    <tr>
      <th>Class</th>
      <th>Precision</th>
      <th>Recall</th>
      <th>F1-Score</th>
      <th>Support</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.0</td>
      <td>0.871134</td>
      <td>0.976879</td>
      <td>0.920981</td>
      <td>173</td>
    </tr>
    <tr>
      <td>1.0</td>
      <td>0.777778</td>
      <td>0.358974</td>
      <td>0.491228</td>
      <td>39</td>
    </tr>
    <tr>
      <td><strong>Accuracy</strong></td>
      <td colspan="4">0.863208</td>
    </tr>
    <tr>
      <td>Macro Avg</td>
      <td>0.824456</td>
      <td>0.667926</td>
      <td>0.706104</td>
      <td>212</td>
    </tr>
    <tr>
      <td>Weighted Avg</td>
      <td>0.853960</td>
      <td>0.863208</td>
      <td>0.841923</td>
      <td>212</td>
    </tr>
  </tbody>
</table>

<h3>Best Parameters from Bayesian Optimization</h3>

<ul>
  <li><strong>n_estimators:</strong> 266</li>
  <li><strong>max_depth:</strong> 11</li>
  <li><strong>min_samples_split:</strong> 2</li>
  <li><strong>min_samples_leaf:</strong> 1</li>
  <li><strong>random_state:</strong> 42</li>
</ul>

📊 **Perbandingan Hasil Evaluasi Model Random Forrest**

Setelah dilakukan Bayesian Optimization, semua metrik evaluasi meningkat secara signifikan.
- Akurasi meningkat dari 84.43% ke 86.32%.
- Presisi meningkat dari 77.23% ke 82.44%, yang berarti model lebih akurat dalam memprediksi karyawan yang benar-benar keluar.
- Recall meningkat dari 62.65% ke 66.79%, artinya model lebih baik dalam menangkap kasus attrition sebenarnya (positif).
- F1-Score, sebagai keseimbangan antara presisi dan recall, juga mengalami peningkatan.

<table border="1">
  <thead>
    <tr>
      <th>Metode</th>
      <th>Akurasi</th>
      <th>Presisi</th>
      <th>Recall</th>
      <th>F1-Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Random Forest</td>
      <td>0.844340</td>
      <td>0.772321</td>
      <td>0.626575</td>
      <td>0.655285</td>
    </tr>
    <tr>
      <td>Random Forest (BayesOpt)</td>
      <td>0.863208</td>
      <td>0.824456</td>
      <td>0.667926</td>
      <td>0.706104</td>
    </tr>
  </tbody>
</table>

🧾 **Kesimpulan Model**
- Bayesian Optimization terbukti meningkatkan kinerja model pada semua metrik evaluasi.
- Model cukup baik untuk klasifikasi karyawan yang tidak keluar, tetapi perlu peningkatan untuk mendeteksi karyawan yang berisiko keluar, misalnya dengan penyesuaian threshold atau teknik handling imbalanced data.
- Parameter hasil tuning dapat digunakan sebagai baseline untuk pengembangan model lebih lanjut.

🔍 **Kesimpulan Utama Analisis**:
1. Model terbaik yang digunakan adalah Random Forest Classifier.
2. Berdasarkan grafik Feature Importance dari model Random Forest, fitur-fitur yang paling berpengaruh dalam menentukan apakah seorang karyawan akan keluar (attrition) yaitu:
    - 🔝 OverTime (Lembur)
        - Penjelasan: Beban kerja berlebih yang berkepanjangan tanpa keseimbangan dapat menimbulkan stres dan burnout, sehingga mendorong keinginan resign.
    - 🏆 StockOptionLevel (Level Opsi Saham)
        - Penjelasan: Karyawan yang memiliki insentif saham cenderung lebih terikat pada perusahaan karena mereka ikut memiliki bagian dalam pertumbuhan bisnis.
    - 🌿 EnvironmentSatisfaction (Kepuasan terhadap Lingkungan Kerja)
        - Penjelasan: Lingkungan kerja yang tidak nyaman atau toxic sering menjadi alasan utama turnover.
    - 😊 JobSatisfaction (Kepuasan Kerja)
        - Penjelasan: Karyawan yang tidak merasa puas dengan pekerjaannya mungkin merasa tidak termotivasi atau tidak dihargai.
    - 🧓 YearsWithCurrManager (Lama bekerja dengan manajer saat ini)
        - Penjelasan: Hubungan yang stabil dengan atasan bisa meningkatkan loyalitas, sebaliknya hubungan yang buruk mempercepat keinginan resign.
    - 💼 TotalWorkingYears
        - Penjelasan: Mereka cenderung memiliki peluang karir lebih baik di tempat lain jika merasa tidak puas.
    - 🧱 JobLevel
        - Penjelasan: Jabatan yang terlalu rendah untuk pengalaman bisa menimbulkan ketidakpuasan. Sebaliknya, level tinggi memiliki beban yang besar.
    - 👥 JobInvolvement (Keterlibatan dalam Pekerjaan)
        - Penjelasan: Ini bisa mencerminkan kurangnya keterikatan atau makna dalam pekerjaan yang dilakukan.
    - 👨‍👩‍👧‍👦 MaritalStatus (Status Pernikahan)
        - Penjelasan: Karyawan menikah mungkin mempertimbangkan faktor stabilitas atau lokasi kerja dalam pengambilan keputusan keluar.
    - 💰 MonthlyIncome (Pendapatan Bulanan)
        - Penjelasan: Pendapatan yang dianggap tidak sebanding dengan beban kerja bisa menyebabkan ketidakpuasan.
3. Notebook juga mempersiapkan dashboard dan koneksi ke database (menggunakan SQLAlchemy dan Supabase) untuk keperluan business monitoring lebih lanjut.

## **Rekomendasi Action Items untuk Perusahaan Jaya Jaya Maju**

🎯 Rekomendasi Bisnis/Action Items:
1. Batasi frekuensi lembur agar dapat membantu menekan tingkat keluar-masuk karyawan.
2. Tingkatkan program-program yang mendukung kepuasan kerja dan keseimbangan antara kehidupan pribadi dan pekerjaan.
3. Tinjau kembali kebijakan kompensasi untuk memastikan pendapatan karyawan sesuai dengan beban kerja.
4. Berikan perhatian khusus pada divisi atau posisi dengan tingkat keterlibatan kerja yang rendah untuk mencegah risiko attrition lebih lanjut.

## 📄 **Executive Summary**

Perusahaan Jaya Jaya Maju mengalami masalah dengan tingginya tingkat attrition (keluar masuk karyawan) yang telah melebihi ambang batas 10%. Untuk mengatasi permasalahan ini, dilakukan proyek analisis data guna mengidentifikasi faktor-faktor utama penyebab attrition serta membangun alat bantu bagi manajemen dalam pengambilan keputusan berbasis data.

Proyek ini menggunakan pendekatan analitik berbasis Python dan data historis karyawan untuk mengeksplorasi pola-pola dalam data, membangun model prediktif, serta membuat dashboard interaktif. Model terbaik yang diperoleh adalah Random Forest Classifier, yang mampu mengidentifikasi potensi karyawan yang berisiko keluar dengan akurasi yang baik.

Faktor-faktor kunci yang ditemukan mempengaruhi attrition antara lain:
<table border="1" cellpadding="8" cellspacing="0">
  <thead>
    <tr>
      <th>Faktor</th>
      <th>Insight Singkat</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>OverTime</td>
      <td>Lembur berlebihan dapat menimbulkan stres dan burnout.</td>
    </tr>
    <tr>
      <td>StockOptionLevel</td>
      <td>Insentif saham meningkatkan rasa memiliki dan loyalitas.</td>
    </tr>
    <tr>
      <td>EnvironmentSatisfaction</td>
      <td>Lingkungan kerja yang tidak nyaman mendorong turnover.</td>
    </tr>
    <tr>
      <td>JobSatisfaction</td>
      <td>Ketidakpuasan kerja menurunkan motivasi dan loyalitas.</td>
    </tr>
    <tr>
      <td>YearsWithCurrManager</td>
      <td>Hubungan baik dengan atasan meningkatkan retensi karyawan.</td>
    </tr>
    <tr>
      <td>TotalWorkingYears</td>
      <td>Pengalaman tinggi membuka peluang pindah ke tempat kerja yang lebih baik.</td>
    </tr>
    <tr>
      <td>JobLevel</td>
      <td>Jabatan yang tidak sesuai pengalaman menimbulkan ketidakpuasan.</td>
    </tr>
    <tr>
      <td>JobInvolvement</td>
      <td>Rendahnya keterlibatan menunjukkan kurangnya makna atau komitmen.</td>
    </tr>
    <tr>
      <td>MaritalStatus</td>
      <td>Status menikah mempengaruhi keputusan keluar karena faktor stabilitas.</td>
    </tr>
    <tr>
      <td>MonthlyIncome</td>
      <td>Gaji yang tidak sesuai beban kerja dapat memicu keinginan resign.</td>
    </tr>
  </tbody>
</table>
Sebagai hasil akhir, data yang telah dibersihkan dan ditransformasi disimpan dalam file `final_dataset.csv`. Selain itu, sistem juga disiapkan untuk koneksi ke database dan pembuatan dashboard agar HR dapat memantau faktor-faktor risiko secara berkelanjutan.
