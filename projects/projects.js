/**
 * Proje listesi — yeni proje eklemek için bu dosyaya kayıt ekleyin.
 * progress: 0–100
 * status: active | planning | completed | paused
 * Sıralama: Aktif → Planlama → Tamamlandı → Duraklatıldı
 */
window.PROJECTS = [
  // —— Aktif ——
  {
    id: 'ahtapot',
    name: 'Ahtapot',
    description: 'E-ticaret platformlarından veri toplayan, düzenleyen ve tek merkezde birleştiren akıllı veri yönetim sistemi.',
    status: 'active',
    progress: 60,
    owner: 'Service Design Development',
    updated: '2026-06-27',
    url: 'projects/ahtapot.html',
    milestones: { completed: 1, total: 3 },
    tags: ['Veri', 'Otomasyon', 'E-ticaret']
  },
  {
    id: 'satici-kazanim',
    name: 'Active Seller',
    description: 'E-ticarette olup n11\'de üye olmayan, yüksek satış potansiyeline sahip satıcıları tespit eden ve puan, ürün adedi, iletişim bilgileri gibi verilerini toplama projesi',
    status: 'active',
    progress: 70,
    owner: 'Murat Özden',
    updated: '2026-07-14',
    url: 'projects/satici-kazanim.html',
    milestones: { completed: 3, total: 5 },
    tags: ['Satıcı Kazanım', 'Trendyol', 'Veri']
  },
  {
    id: 'iframe',
    name: 'Iframe → Native Render',
    description: 'Legal sayfalardaki iframe kullanımını kaldırıp native render\'a geçmek; E-E-A-T sinyallerini güçlendirmek ve forum tarzı bilgi aramalarına ürün destekli içerik sayfalarıyla organik trafik yakalamak.',
    status: 'active',
    progress: 25,
    owner: 'Service Design Development',
    updated: '2026-06-27',
    url: 'projects/iframe.html',
    milestones: { completed: 0, total: 5 },
    tags: ['SEO', 'E-E-A-T', 'Organik Trafik']
  },
  {
    id: 'structureddata',
    name: 'Structured Data',
    description: 'n11.com ürün detay sayfalarına Schema.org yapılandırılmış veri ekleyerek arama motorları ve yapay zeka sistemlerinin ürünleri doğru anlamasını sağlayan etiketleme projesi.',
    status: 'active',
    progress: 40,
    owner: 'Service Design Development',
    updated: '2026-06-27',
    url: 'projects/structured-data.html',
    milestones: { completed: 1, total: 4 },
    tags: ['Schema.org', 'SEO', 'LLM']
  },
  // —— Planlama ——
  {
    id: 'attribute',
    name: 'Attribute',
    description: 'n11 PDP ürün attribute verisini Akakçe, Hepsiburada, Trendyol gibi platformlardan çekip eşleştirme, mapping ve aktarım ile genişletmeyi hedefleyen proje. İlk faz: Akakçe.',
    status: 'planning',
    progress: 0,
    owner: 'Murat Özden',
    updated: '2026-07-13',
    url: 'projects/attribute.html',
    milestones: { completed: 0, total: 4 },
    tags: ['Attribute', 'Akakçe', 'PDP']
  },
  {
    id: 'seller-importer',
    name: 'Seller Importer',
    description: 'n11\'e katılmak isteyen satıcıların Trendyol mağaza sayfasını tarayıp ürün kataloğunu toplayan, n11\'e aktaran ve ürünleri hazır tanımlı hesap sunan proje. Active Seller\'ın devamı.',
    status: 'active',
    progress: 5,
    owner: 'Murat Özden',
    updated: '2026-07-14',
    url: 'projects/seller-importer.html',
    milestones: { completed: 0, total: 4 },
    tags: ['Satıcı Kazanım', 'Trendyol', 'Ürün Aktarımı']
  },
  {
    id: 'search-journeys',
    name: 'Search Journeys',
    description: 'Araştır → karşılaştır → karar ver → satın al yolculuğunu destekleyen editöryal rehber sayfaları. Helpful Content ve E-E-A-T odaklı; 3–5 ürün, LLM üretimi yok, 6 ayda bir güncelleme.',
    status: 'planning',
    progress: 0,
    owner: 'Service Design Development',
    updated: '2026-07-13',
    url: 'projects/search-journeys.html',
    milestones: { completed: 0, total: 4 },
    tags: ['SEO', 'E-E-A-T', 'Helpful Content']
  },
  {
    id: 'user-dna',
    name: 'User DNA Hyper-Personalization',
    description: 'Kullanıcıyı kategori ve yaşam tarzı verileriyle tanıyarak one-click kişiselleştirilmiş listeler sunan proje. E-E-A-T Experience & Trust; stok vitrininden uzman platforma geçiş.',
    status: 'planning',
    progress: 0,
    owner: 'Service Design Development',
    updated: '2026-07-13',
    url: 'projects/user-dna.html',
    milestones: { completed: 0, total: 4 },
    tags: ['Personalization', 'E-E-A-T', 'Experience']
  },
  {
    id: 'programmatic-search-listing',
    name: 'Programmatic Search Listing',
    description: 'LLM ile ürünleri intent etiketleriyle işaretleyip clean URL listing sayfaları ve sitemap üreten SEO projesi. Organik + searchbar; rakipsiz SERP yüzeyi ve crawl budget verimliliği.',
    status: 'planning',
    progress: 0,
    owner: 'Service Design Development',
    updated: '2026-07-13',
    url: 'projects/programmatic-search-listing.html',
    milestones: { completed: 0, total: 4 },
    tags: ['SEO', 'LLM', 'SERP']
  },
  {
    id: 'programmatic-group-listing',
    name: 'Programmatic Group Listing',
    description: 'PSL etiketlerini senaryo bazlı grup rehberlerine taşıyan proje. Yeni ev / bebek odası gibi long-tail sayfalar; kategori başına 3 ürün, dinamik besleme, SEO URL→Title→SD zinciri.',
    status: 'planning',
    progress: 0,
    owner: 'Service Design Development',
    updated: '2026-07-13',
    url: 'projects/programmatic-group-listing.html',
    milestones: { completed: 0, total: 4 },
    tags: ['SEO', 'Grup Listeleme', 'Long-tail']
  },
  {
    id: 'llm-spam-guardrail',
    name: 'LLM Spam Guardrail (Over-optimization)',
    description: 'Title/heading’de clickbait, keyword stuffing ve içerikle örtüşmeyen abartılı ifadeleri LLM ile tespit edip Seller Office’te temiz title öneren SEO koruma katmanı.',
    status: 'planning',
    progress: 0,
    owner: 'Service Design Development',
    updated: '2026-07-13',
    url: 'projects/llm-spam-guardrail.html',
    milestones: { completed: 0, total: 3 },
    tags: ['LLM', 'SEO', 'YMYL']
  },
  {
    id: 'UCP',
    name: 'UCP',
    description: 'Yapılandırılmış veri; n11.com\'u yapay zeka (LLM) ve arama botlarının kolayca anlayıp önermesini sağlayan etiketleme projesi',
    status: 'planning',
    progress: 0,
    owner: 'Service Design Development',
    updated: '2026-06-27',
    url: null,
    milestones: { completed: 1, total: 4 },
    tags: ['LLM', 'Organik Trafik']
  },
  // —— Tamamlandı ——
  {
    id: 'abtest',
    name: 'A/B Test Tool',
    description: 'n11.com A/B optimizasyon testlerini planlamak, önizlemek ve takip etmek için tamamen in-house geliştirilmiş platform. 1,5+ yıldır canlıda; kendi database yapısı ve uçtan uca test süreci yönetimi.',
    status: 'completed',
    progress: 100,
    owner: 'Doğan Yılmaz',
    updated: '2026-06-27',
    url: 'projects/ab-test-tool.html',
    milestones: { completed: 4, total: 4 },
    tags: ['A/B Test', 'Optimizasyon', 'In-house']
  },
  {
    id: 'bo-version-control',
    name: 'Backoffice Version Kontrol',
    description: 'Backoffice CMS\'te statik sayfa ve kampanyalar için versiyon geçmişi; paralel revize taleplerinde kod çakışmasını önler ve istenen tarih/versiyona geri dönüş sağlar.',
    status: 'completed',
    progress: 100,
    owner: 'Tuğba Özbek',
    updated: '2026-06-27',
    url: 'projects/backoffice-version-control.html',
    milestones: { completed: 2, total: 2 },
    tags: ['Backoffice', 'CMS', 'Version Control']
  },
  {
    id: 'html-campaign-orderer',
    name: 'HTML Campaign Orderer',
    description: '500 markalı kampanya sayfalarında günlük sıralama değişikliklerini HTML içinde manuel taşımak yerine otomatik düzenleyen araç.',
    status: 'completed',
    progress: 100,
    owner: 'Tuğba Özbek',
    updated: '2026-06-27',
    url: 'projects/html-campaign-orderer.html',
    milestones: { completed: 2, total: 2 },
    tags: ['Kampanya', 'Sıralama', 'Otomasyon']
  },
  {
    id: 'otomatik-kampanya',
    name: 'Otomatik Kampanya Sayfa Oluşturma',
    description: 'Growth ve kategori ekiplerinin Excel ile ilettiği kampanya verilerinden kampanya sayfası HTML\'ini otomatik üreten sistem. Saatler süren manuel süreç saniyelere indi.',
    status: 'completed',
    progress: 100,
    owner: 'Tuğba Özbek',
    updated: '2026-06-27',
    url: 'projects/otomatik-kampanya-sayfa.html',
    milestones: { completed: 3, total: 3 },
    tags: ['Kampanya', 'Excel', 'Otomasyon']
  },
  {
    id: 'extension',
    name: 'Productivity Extension',
    description: 'Şirket içi departmanlarımızı hızlandırmak, rutin görevleri otomatize etmek ve operasyonel verimliliği maksimuma çıkarmak için geliştirilmiş tarayıcı/sistem eklenti projesi.',
    status: 'active',
    progress: 99,
    owner: 'Murat Özden',
    updated: '2026-06-27',
    url: 'projects/productivity-extension.html',
    milestones: { completed: 41, total: 41 },
    tags: ['Chrome Extension', 'Otomasyon', 'Verimlilik']
  }
];
