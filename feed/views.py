from django.shortcuts import render

# Create your views here.
# Suggested code may be subject to a license. Learn more: ~LicenseLog:392275320.
def index(request):
    artickel_data = {
        'artikel 1': {
        'title': 'Artikel ini sangat berguna',
        'date': '23-04-2023',
        'category': 'Buku',
        'simple_content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
    },
    'artikel 2': {
        'title': 'Panduan Lengkap Memilih Laptop untuk Programming',
        'date': '10-05-2023',
        'category': 'Teknologi',
        'simple_content': 'Memilih laptop yang tepat untuk programming bisa jadi membingungkan. Artikel ini akan membahas spesifikasi penting yang perlu diperhatikan.'
    },
    'artikel 3': {
        'title': 'Resep Kue Coklat Mudah untuk Pemula',
        'date': '15-05-2023',
        'category': 'Masakan',
        'simple_content': 'Ingin membuat kue coklat yang lezat? Ikuti resep mudah ini dan nikmati kue coklat buatan sendiri yang sempurna.'
    },
    'artikel 4': {
        'title': '5 Tips Menjaga Kesehatan Mental di Era Digital',
        'date': '22-05-2023',
        'category': 'Kesehatan',
        'simple_content': 'Kehidupan digital dapat berdampak pada kesehatan mental kita. Artikel ini memberikan tips untuk menjaga keseimbangan dan kesejahteraan mental.'
    },
    'artikel 5': {
        'title': 'Review Film Terbaru: Aksi yang Menegangkan!',
        'date': '29-05-2023',
        'category': 'Hiburan',
        'simple_content': 'Film terbaru ini menawarkan aksi yang menegangkan dan plot yang menarik. Simak review lengkapnya di sini.'
    },
    'artikel 6': {
        'title': 'Review Film Terbaru: Sebuah Pencapaian',
        'date': '29-05-2023',
        'category': 'Hiburan',
        'simple_content': 'Film terbaru ini menawarkan aksi yang menegangkan dan plot yang menarik. Simak review lengkapnya di sini.'
    },
    }
    context = {
        'artickel_data': artickel_data,
    }
    
    return render(request, 'home/index.html',context)