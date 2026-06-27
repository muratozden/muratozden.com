/**
 * Proje listesi — yeni proje eklemek için bu dosyaya kayıt ekleyin.
 * progress: 0–100
 * status: active | planning | completed | paused
 */
window.PROJECTS = [
  {
    id: 'ahtapot',
    name: 'Ahtapot',
    description: 'E-ticaret platformlarından veri toplayan, düzenleyen ve tek merkezde birleştiren akıllı veri yönetim sistemi.',
    status: 'active',
    progress: 20,
    owner: 'Service Design Development',
    updated: '2026-06-27',
    url: 'projects/ahtapot.html',
    milestones: { completed: 1, total: 3 },
    tags: ['Veri', 'Otomasyon', 'E-ticaret']
  },
  {
    id: 'abtest',
    name: 'A/B Test Tool',
    description: 'n11.com A/B optimizasyon testlerini planlamak, önizlemek ve takip etmek için tamamen in-house geliştirilmiş platform. 1,5+ yıldır canlıda; kendi database yapısı ve uçtan uca test süreci yönetimi.',
    status: 'completed',
    progress: 85,
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
    status: 'active',
    progress: 80,
    owner: 'Tuğba Özbek',
    updated: '2026-06-27',
    url: 'projects/backoffice-version-control.html',
    milestones: { completed: 3, total: 4 },
    tags: ['Backoffice', 'CMS', 'Version Control']
  },
  {
    id: 'extension',
    name: 'Productivity Extension',
    description: 'Şirket içi departmanlarımızı hızlandırmak, rutin görevleri otomatize etmek ve operasyonel verimliliği maksimuma çıkarmak için geliştirilmiş tarayıcı/sistem eklenti projesi.',
    status: 'completed',
    progress: 100,
    owner: 'Murat Özden',
    updated: '2026-06-27',
    url: 'projects/productivity-extension.html',
    milestones: { completed: 41, total: 41 },
    tags: ['Chrome Extension', 'Otomasyon', 'Verimlilik']
  },
  {
    id: 'structureddata',
    name: 'Structured Data',
    description: 'n11.com ürün detay sayfalarına Schema.org yapılandırılmış veri ekleyerek arama motorları ve yapay zeka sistemlerinin ürünleri doğru anlamasını sağlayan etiketleme projesi.',
    status: 'active',
    progress: 10,
    owner: 'Service Design Development',
    updated: '2026-06-27',
    url: 'projects/structured-data.html',
    milestones: { completed: 1, total: 4 },
    tags: ['Schema.org', 'SEO', 'LLM']
  },
  {
    id: 'iframe',
    name: 'Iframe → Native Render',
    description: 'Legal sayfalardaki iframe kullanımını kaldırıp native render\'a geçmek; E-E-A-T sinyallerini güçlendirmek ve forum tarzı bilgi aramalarına ürün destekli içerik sayfalarıyla organik trafik yakalamak.',
    status: 'active',
    progress: 5,
    owner: 'Service Design Development',
    updated: '2026-06-27',
    url: 'projects/iframe.html',
    milestones: { completed: 0, total: 5 },
    tags: ['SEO', 'E-E-A-T', 'Organik Trafik']
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
  }
];
