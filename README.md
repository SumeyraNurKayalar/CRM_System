-------Müşteri Temsilcisi Atama-------
def assign_representatives(cost_matrix): müşteri ve temsilci arası maaliyet matrisini (cost_matrix) girdi olarak alır.
n = len(cost_matrix) temsilci sayısını verir.
m = len(cost_matrix[0]) müşteri sayısını verir.
assigned = set() ile atanmış temsilcileri talip eden küme oluşturulur.
assignments = [] ile atamaları tutacak olan liste oluşturulur.
 total_cost = 0 ile toplam maaliyet en başta sıfır olarak tanımlanır.
for cust in range(m): # O(m) her müşteri için en düşük maaliyeli temsilciyi bulacak bir döngü oluşturulur.
min_cost = float('inf') ile en düşük maaliyeti başta sonsuz olarakk belirleriz.
best_rep = -1 ile en iyi temsilciyi tutan değişken oluşturulur.
for rep in range(n): ile her müşteri için tüm temsilcileri kontrol edecek bir döngü oluşturulur.
if rep not in assigned and cost_matrix[rep][cust] < min_cost: satırında eğer temsilci atanmışsa o temsilciyi atlayarak diğer temsilcilere bakılması sağlanır. Eğer mevcut temsilcinin maaliyeti önceki minimum maaliyetten küçükse onu yeni aday olarak seçer.
min_cost = cost_matrix[rep][cust] ile en düşük maaliyet bulunur.
best_rep = rep ile ise en iyi temsilci güncellenir.
if best_rep != -1: satırı ile eğer bir müşteri için uygun bir temsilci bulunmuşsa işlem devam ettirilir.
assigned.add(best_rep) ile temsilci atananlar listesine ekklenir.
assignments.append((best_rep + 1, cust + 1)) ile temsilci müşteri eşleşmesini saklar.
total_cost += min_cost ile toplam maaliyet güncellenir.
return assignments, total_cost ile atanan temsilci/müşteri çiftleri ve toplam atama maliyeti döndürülür.

-------Knapsack Problemi ile Pazarlama Kampanyası Seçimi-------
def knapsack(budget, costs, profits): fonksiyonuyla kullanılabilir maksimum bütçe, kampanya maaliyetleri, kampanyanın getirdiği karların girdileri alınır.
n = len(costs) ile kampanya sayısı alınır.
dp = [[0] * (budget + 1) for _ in range(n + 1)] ile DP tablosu oluşturulur.
for i in range(1, n + 1): ve for b in range(budget + 1): ile her kampanya ve bütçe için çözüm hesaplanır.
if costs[i - 1] <= b: ile döngü kampanya maaaliyeti bütçeyi aşmadığı koşullarda çalıştırılır.
 dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - costs[i - 1]] + profits[i - 1]) satırı kapmanyayı seçmek için kullanılır.
else: dp[i][b] = dp[i - 1][b] ile eğer kampanya bütçeyi aşarsa sadece dp[i-1][b]seçilmesi sağlanır.
b = budget ile be değişkenine bütçe atanır.
for i in range(n, 0, -1): kampanyaları tersten kontrol etmek için bir döngü başlatır.
if dp[i][b] != dp[i - 1][b]: ile eğer i numaralı kampanya seçildiyse içeri girişs sağlanır.
selected_campaigns.append(i - 1) ile seçilen kampanyanın maaliyetini bütçeden düşülerek kalan bütçe güncellenir.
b -= costs[i - 1] ile seçilen kampanyanın maaliyeri bütçeden düşülerek kalan bütçe güncellenir.
return dp[n][budget], selected_campaigns ile en yüksek kazanç ve seçilen kampanya numaraları döndürülür.
