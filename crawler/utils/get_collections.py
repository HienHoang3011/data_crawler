def gen_links_1(chuong, start_id, so_de, lop, mon):
    return [
        f"https://loigiaihay.com/de-kiem-tra-15-phut-chuong-{chuong}-de-so-{i}-dai-so-va-giai-tich-{lop}-c46a{start_id + i - 1}.html"
        for i in range(1, so_de + 1)
    ]
    
def create_collection_link_math():
    collection_math = []
    link_chuong_1_11_15p = gen_links_1(chuong=1, start_id=45788, so_de=10, lop=11, mon='math')
    link_chuong_2_11_15p = gen_links_1(chuong=2, start_id=45832, so_de=9, lop=11, mon='math')
    link_chuong_3_11_15p = gen_links_1(chuong=3, start_id=50032, so_de=3, lop=11, mon='math')
    link_chuong_4_11_15p = gen_links_1(chuong=4, start_id=46489, so_de=8, lop=11, mon='math')
    link_chuong_5_11_15p = gen_links_1(chuong=5, start_id=46507, so_de=5, lop=11, mon='math')
    link_chuong_1_11_45p = gen_links_1(chuong=1, start_id=45827, so_de=5, lop=11, mon='math')
    link_chuong_2_11_45p = gen_links_1(chuong=2, start_id=45852, so_de=5, lop=11, mon='math')
    link_chuong_3_11_45p = gen_links_1(chuong=3, start_id=50035, so_de=2, lop=11, mon='math')
    link_chuong_4_11_45p = gen_links_1(chuong=4, start_id=46497, so_de=4, lop=11, mon='math')
    link_chuong_5_11_45p = gen_links_1(chuong=5, start_id=46687, so_de=5, lop=11, mon='math')
    link_math_11 = link_chuong_1_11_15p + link_chuong_2_11_15p + link_chuong_3_11_15p + link_chuong_4_11_15p + link_chuong_5_11_15p
    link_math_11 += link_chuong_1_11_45p + link_chuong_2_11_45p + link_chuong_3_11_45p + link_chuong_4_11_45p + link_chuong_5_11_45p
    collection_math.extend(link_math_11)
    link_chuong_1_12_15p = gen_links_1(chuong=1, start_id=44772, so_de=5, lop=12, mon='math')
    link_chuong_2_12_15p = gen_links_1(chuong=2, start_id=44791, so_de=5, lop=12, mon='math')
    link_chuong_3_12_15p = gen_links_1(chuong=3, start_id=47413, so_de=5, lop=12, mon='math')
    link_chuong_4_12_15p = gen_links_1(chuong=4, start_id=47424, so_de=5, lop=12, mon='math')
    link_chuong_1_12_45p = gen_links_1(chuong=1, start_id=44796, so_de=5, lop=12, mon='math')
    link_chuong_2_12_45p = gen_links_1(chuong=2, start_id=44808, so_de=4, lop=12, mon='math')
    link_chuong_3_12_45p = gen_links_1(chuong=3, start_id=47429, so_de=5, lop=12, mon='math')
    link_chuong_4_12_45p = gen_links_1(chuong=4, start_id=47438, so_de=5, lop=12, mon='math')
    link_math_12 = link_chuong_1_12_15p + link_chuong_2_12_15p + link_chuong_3_12_15p + link_chuong_4_12_15p
    link_math_12 += link_chuong_1_12_45p + link_chuong_2_12_45p + link_chuong_3_12_45p + link_chuong_4_12_45p
    collection_math.extend(link_math_12)
    return collection_math


def create_collection_link_math_6():
    collection_math_6 = []
    collection_math_6_gk1 = [
        "https://loigiaihay.com/de-kiem-tra-giua-hoc-ki-1-toan-6-de-so-1-ket-noi-tri-thuc-a120884.html",
        "https://loigiaihay.com/de-kiem-tra-giua-hoc-ki-1-toan-6-de-so-2-ket-noi-tri-thuc-a120989.html",
        "https://loigiaihay.com/de-kiem-tra-giua-hoc-ki-1-toan-6-de-so-3-ket-noi-tri-thuc-a121331.html",
        "https://loigiaihay.com/de-kiem-tra-giua-hoc-ki-1-toan-6-de-so-4-ket-noi-tri-thuc-a121886.html",
        "https://loigiaihay.com/de-kiem-tra-giua-hoc-ki-1-toan-6-de-so-5-ket-noi-tri-thuc-a122030.html",
        "https://loigiaihay.com/de-kiem-tra-giua-hoc-ki-1-toan-6-de-so-6-ket-noi-tri-thuc-a151756.html",
        "https://loigiaihay.com/de-kiem-tra-giua-hoc-ki-1-toan-6-de-so-7-ket-noi-tri-thuc-a151757.html",
        "https://loigiaihay.com/de-kiem-tra-giua-hoc-ki-1-toan-6-de-so-8-ket-noi-tri-thuc-a151760.html",
        "https://loigiaihay.com/de-kiem-tra-giua-hoc-ki-1-toan-6-de-so-9-ket-noi-tri-thuc-a151761.html",
        "https://loigiaihay.com/de-kiem-tra-giua-hoc-ki-1-toan-6-de-so-10-ket-noi-tri-thuc-a151762.html",
        "https://loigiaihay.com/de-kiem-tra-giua-hoc-ki-1-toan-6-de-so-11-ket-noi-tri-thuc-a151830.html",
        "https://loigiaihay.com/de-kiem-tra-giua-hoc-ki-1-toan-6-de-so-12-ket-noi-tri-thuc-a151831.html",
        "https://loigiaihay.com/de-kiem-tra-giua-hoc-ki-1-toan-6-de-so-13-ket-noi-tri-thuc-a151834.html",
        "https://loigiaihay.com/de-kiem-tra-giua-hoc-ki-1-toan-6-de-so-14-ket-noi-tri-thuc-a151835.html",
        "https://loigiaihay.com/de-kiem-tra-giua-hoc-ki-1-toan-6-de-so-15-ket-noi-tri-thuc-a151836.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-6-de-so-16-a176470.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-6-de-so-17-a176471.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-6-de-so-18-a176472.html"
    ]
    collection_math_6_hk1 = [
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-1-toan-6-de-so-1-ket-noi-tri-thuc-a123788.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-1-toan-6-de-so-2-ket-noi-tri-thuc-a123841.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-1-toan-6-de-so-3-ket-noi-tri-thuc-a123914.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-1-toan-6-de-so-4-ket-noi-tri-thuc-a124010.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-1-toan-6-de-so-5-ket-noi-tri-thuc-a124078.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-1-toan-6-de-so-6-ket-noi-tri-thuc-a124702.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-1-toan-6-de-so-7-ket-noi-tri-thuc-a124703.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-1-toan-6-de-so-8-ket-noi-tri-thuc-a124721.html", 
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-1-toan-6-de-so-9-ket-noi-tri-thuc-a124726.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-1-toan-6-de-so-10-ket-noi-tri-thuc-a131900.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-1-toan-6-de-so-11-ket-noi-tri-thuc-a153108.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-1-toan-6-de-so-12-ket-noi-tri-thuc-a153109.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-1-toan-6-de-so-13-ket-noi-tri-thuc-a153110.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-1-toan-6-de-so-14-ket-noi-tri-thuc-a153112.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-1-toan-6-de-so-15-ket-noi-tri-thuc-a153113.html",
        "http://loigiaihay.com/de-thi-hoc-ki-1-toan-6-de-so-16-a179462.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-6-de-so-17-a179463.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-6-de-so-18-a179465.html"
    ]
    collection_math_6_gk2 = [
        "https://loigiaihay.com/de-kiem-tra-giua-hoc-ki-2-toan-6-de-so-1-ket-noi-tri-thuc-a133534.html",
        "https://loigiaihay.com/de-kiem-tra-giua-hoc-ki-2-toan-6-de-so-2-ket-noi-tri-thuc-a133562.html",
        "https://loigiaihay.com/de-kiem-tra-giua-hoc-ki-2-toan-6-de-so-3-ket-noi-tri-thuc-a133563.html",
        "https://loigiaihay.com/de-kiem-tra-giua-hoc-ki-2-toan-6-de-so-4-ket-noi-tri-thuc-a133615.html",
        "https://loigiaihay.com/de-kiem-tra-giua-hoc-ki-2-toan-6-de-so-5-ket-noi-tri-thuc-a133683.html",
        "https://loigiaihay.com/de-thi-giua-ki-2-toan-6-ket-noi-tri-thuc-de-so-6-a155856.html",
        "https://loigiaihay.com/de-thi-giua-ki-2-toan-6-ket-noi-tri-thuc-de-so-7-a155857.html",
        "https://loigiaihay.com/de-thi-giua-ki-2-toan-6-ket-noi-tri-thuc-de-so-8-a155858.html",
        "https://loigiaihay.com/de-thi-giua-ki-2-toan-6-ket-noi-tri-thuc-de-so-9-a155859.html",
        "https://loigiaihay.com/de-thi-giua-ki-2-toan-6-ket-noi-tri-thuc-de-so-10-a155860.html"
    ]
    collection_math_6_hk2 = [
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-2-toan-6-de-so-1-ket-noi-tri-thuc-a134618.html",
        'https://loigiaihay.com/de-kiem-tra-hoc-ki-2-toan-6-de-so-2-ket-noi-tri-thuc-a134733.html',
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-2-toan-6-de-so-3-ket-noi-tri-thuc-a134927.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-2-toan-6-de-so-4-ket-noi-tri-thuc-a135292.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-2-toan-6-de-so-5-ket-noi-tri-thuc-a135613.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-2-toan-6-de-so-6-ket-noi-tri-thuc-a136660.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-2-toan-6-de-so-7-ket-noi-tri-thuc-a136934.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-2-toan-6-de-so-8-ket-noi-tri-thuc-a137089.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-2-toan-6-de-so-9-ket-noi-tri-thuc-a137243.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-2-toan-6-de-so-10-ket-noi-tri-thuc-a137334.html",
        "https://loigiaihay.com/de-thi-hoc-ki-2-toan-6-de-so-11-ket-noi-tri-thuc-a160547.html",
        "https://loigiaihay.com/de-thi-hoc-ki-2-toan-6-de-so-12-ket-noi-tri-thuc-a160548.html",
        "https://loigiaihay.com/de-thi-hoc-ki-2-toan-6-de-so-13-ket-noi-tri-thuc-a160549.html"
    ]
    collection_math_6 += collection_math_6_gk1 + collection_math_6_hk1 + collection_math_6_gk2 + collection_math_6_hk2
    return collection_math_6
    
        
def create_collection_link_math_10():
    collection_math_10 = [
        "https://loigiaihay.com/de-khao-sat-chat-luong-dau-nam-lop-10-mon-toan-de-so-2-a113801.html",
        "https://loigiaihay.com/de-khao-sat-chat-luong-dau-nam-lop-10-mon-toan-de-so-4-a113803.html"
    ]
    link_math_10_gk1 = [
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-ket-noi-tri-thuc-de-so-1-a121902.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-ket-noi-tri-thuc-de-so-2-a122128.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-ket-noi-tri-thuc-de-so-3-a122129.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-ket-noi-tri-thuc-de-so-4-a122130.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-de-so-6-a152176.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-ket-noi-tri-thuc-de-so-6-a152177.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-ket-noi-tri-thuc-de-so-7-a152188.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-ket-noi-tri-thuc-de-so-8-a152197.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-ket-noi-tri-thuc-de-so-9-a152203.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-ket-noi-tri-thuc-de-so-10-a152210.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-ket-noi-tri-thuc-de-so-11-a176248.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-ket-noi-tri-thuc-de-so-12-a176249.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-ket-noi-tri-thuc-de-so-13-a176250.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-de-so-14-a188967.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-de-so-15-a188972.html"
    ]
    link_math_10_gk1 += [
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-10-ket-noi-tri-thuc-de-so-1-a124204.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-10-ket-noi-tri-thuc-de-so-2-a124237.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-10-ket-noi-tri-thuc-de-so-3-a124238.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-10-ket-noi-tri-thuc-de-so-4-a124240.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-10-ket-noi-tri-thuc-de-so-5-a124393.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-10-ket-noi-tri-thuc-de-so-6-a124394.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-10-ket-noi-tri-thuc-de-so-6-a124395.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-10-ket-noi-tri-thuc-de-so-9-a124425.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-10-ket-noi-tri-thuc-de-so-9-a124426.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-10-ket-noi-tri-thuc-de-so-11-a178718.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-10-ket-noi-tri-thuc-de-so-11-a178719.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-10-ket-noi-tri-thuc-de-so-11-a178720.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-10-ket-noi-tri-thuc-de-so-15-a189469.html"
    ]
    link_math_10_gk2 = [
        "https://loigiaihay.com/de-thi-giua-ki-2-toan-10-ket-noi-tri-thuc-de-so-1-a156395.html",
        "https://loigiaihay.com/de-thi-giua-ki-2-toan-10-ket-noi-tri-thuc-de-so-2-a156399.html",
        "https://loigiaihay.com/de-thi-giua-ki-2-toan-10-ket-noi-tri-thuc-de-so-3-a156400.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-2-toan-10-de-so-1-ket-noi-tri-thuc-a134980.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-2-toan-10-de-so-ket-noi-tri-thuc-a135043.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-2-toan-10-de-so-3-ket-noi-tri-thuc-a135044.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-2-toan-10-de-so-4-ket-noi-tri-thuc-a135046.html",
        
    ]
    collection_math_10 += link_math_10_gk1
    collection_math_10 += link_math_10_gk2
    return collection_math_10

def create_collection_chemical_10():
    collection_chemical_10 = [
        "https://loigiaihay.com/de-thi-giua-ki-1-hoa10-ket-noi-tri-thuc-e28627.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-hoa-10-ket-noi-tri-thuc-de-so-1-a121366.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-hoa-10-ket-noi-tri-thuc-de-so-2-a121370.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-hoa-10-ket-noi-tri-thuc-de-so-3-a121374.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-hoa-10-ket-noi-tri-thuc-de-so-4-a121378.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-hoa-10-ket-noi-tri-thuc-de-so-5-a121478.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-hoa-10-ket-noi-tri-thuc-de-so-6-a151066.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-hoa-10-ket-noi-tri-thuc-de-so-7-a151067.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-hoa-10-ket-noi-tri-thuc-de-so-8-a151068.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-hoa-10-ket-noi-tri-thuc-de-so-9-a151075.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-hoa-10-ket-noi-tri-thuc-de-so-10-a151078.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-hoa-10-ket-noi-tri-thuc-de-so-11-a173804.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-hoa-10-ket-noi-tri-thuc-de-so-12-a173811.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-hoa-10-ket-noi-tri-thuc-de-so-13-a173854.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-hoa-10-ket-noi-tri-thuc-de-so-14-a189050.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-hoa-10-ket-noi-tri-thuc-de-so-15-a189051.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-hoa-10-ket-noi-tri-thuc-e34166.html",
        "https://loigiaihay.com/de-cuong-on-tap-hk1-hoa-10-co-dap-an-a152802.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-hoa-10-ket-noi-tri-thuc-de-so-1-a152647.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-hoa-10-ket-noi-tri-thuc-de-so-2-a152649.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-hoa-10-ket-noi-tri-thuc-de-so-3-a152650.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-hoa-10-ket-noi-tri-thuc-de-so-4-a152651.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-hoa-10-ket-noi-tri-thuc-de-so-5-a152653.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-hoa-10-ket-noi-tri-thuc-de-so-6-a153046.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-hoa-10-ket-noi-tri-thuc-de-so-7-a177428.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-hoa-10-ket-noi-tri-thuc-de-so-8-a177451.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-hoa-10-ket-noi-tri-thuc-de-so-9-a177573.html",
        "https://loigiaihay.com/de-thi-giua-ki-2-hoa-10-ket-noi-tri-thuc-e34739.html",
        "https://loigiaihay.com/de-thi-giua-ki-2-hoa-10-ket-noi-tri-thuc-de-so-1-a155038.html",
        "https://loigiaihay.com/de-thi-giua-ki-2-hoa-10-ket-noi-tri-thuc-de-so-2-a155043.html",
        "https://loigiaihay.com/de-thi-giua-ki-2-hoa-10-ket-noi-tri-thuc-de-so-3-a155044.html",
        "https://loigiaihay.com/de-thi-giua-ki-2-hoa-10-ket-noi-tri-thuc-de-so-4-a155082.html",
        "https://loigiaihay.com/de-thi-giua-ki-2-hoa-10-ket-noi-tri-thuc-de-so-5-a155083.html",
        "https://loigiaihay.com/de-thi-giua-ki-2-hoa-10-ket-noi-tri-thuc-de-so-6-a156787.html",
        "https://loigiaihay.com/de-thi-giua-ki-2-hoa-10-ket-noi-tri-thuc-de-so-7-a156861.html",
        "https://loigiaihay.com/de-thi-giua-ki-2-hoa-10-ket-noi-tri-thuc-de-so-8-a156863.html",
        "https://loigiaihay.com/de-thi-hoc-ki-2-hoa-10-ket-noi-tri-thuc-e31300.html",
        "https://loigiaihay.com/de-cuong-on-tap-hk2-hoa-10-co-dap-an-a158859.html",
        "https://loigiaihay.com/de-thi-hoc-ki-2-hoa-hoc-10-ket-noi-tri-thuc-de-1-a136735.html",
        "https://loigiaihay.com/de-thi-hoc-ki-2-hoa-11-ket-noi-tri-thuc-de-2-a136810.html",
        "https://loigiaihay.com/de-thi-hoc-ki-2-hoa-11-ket-noi-tri-thuc-de-3-a136827.html",
        "https://loigiaihay.com/de-thi-hoc-ki-2-hoa-11-ket-noi-tri-thuc-de-4-a137000.html",
        "https://loigiaihay.com/de-thi-hoc-ki-2-hoa-10-ket-noi-tri-thuc-de-5-a137036.html",
        "https://loigiaihay.com/de-thi-hoc-ki-2-hoa-10-ket-noi-tri-thuc-de-so-1-a158865.html",
        "https://loigiaihay.com/de-thi-hoc-ki-2-hoa-10-ket-noi-tri-thuc-de-so-7-a158866.html",
        "https://loigiaihay.com/de-thi-hoc-ki-2-hoa-10-ket-noi-tri-thuc-de-so-8-a158872.html"
    ]
    return collection_chemical_10