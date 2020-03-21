# from http.cookies import SimpleCookie
from urllib.parse import urlparse, parse_qs, urlencode


URL = 'https://www.emag.ro/search-by-url?source_id=7&templates%5B%5D=full&is_eab49=false&sort%5Bpopularity%5D=desc&listing_display_id=2&page%5Blimit%5D=60&page%5Boffset%5D=60&fields%5Bitems%5D%5Bimage_gallery%5D%5Bfashion%5D%5Blimit%5D=2&fields%5Bitems%5D%5Bimage%5D%5Bresized_images%5D=1&fields%5Bitems%5D%5Bresized_images%5D=200x200%2C350x350&fields%5Bitems%5D%5Bfamily%5D=1&fields%5Bitems%5D%5Bflags%5D=1&fields%5Bitems%5D%5Boffer%5D%5Bbuying_options%5D=1&fields%5Bitems%5D%5Boffer%5D%5Bflags%5D=1&fields%5Bitems%5D%5Boffer%5D%5Bbundles%5D=1&fields%5Bitems%5D%5Boffer%5D%5Bgifts%5D=1&fields%5Bquick_filters%5D=1&search_id=d27c0b387b234a5b494d&search_fraze=&search_key=a4e5afc34d23c6d5fa89a21908d1ae6d&url=%2Ftelefoane-mobile%2Fc'

# def cookie_parser():
#     cookie_string = 'EMAGVISITOR=a%3A1%3A%7Bs%3A7%3A%22user_id%22%3Bi%3A2806796647%3B%7D; ltuid=1548105346.647-e11654252febd8abb0c49168486f3e52b18859d7; _ga=GA1.2.929026208.1548105347; G_ENABLED_IDPS=google; gr_reco=1687bce0820-cf5e1da9ed4d0da1; listingPerPage=60; listingDisplayId=2; EMAGUUID=1560506377-330850005-74519.038; sr=1920x1040; vp=1920x937; _hjid=5139716d-9d11-4040-a2e6-45a748260501; ga_user_id=69024df7e0e9ac153fa4de81837ad619; user_token=4a7503aad1881cc5947d53257b03c943; customer_has_orders=1; keep_after_logout=%DB%11b%C5dy%B9%BA%EC%01E%B6n%DA%C0%03%9A%B0%1D7%0DE%E5j%C4%84%EF%23M%B9%7E%CE%8B%0E%29W%40%09%D8%94%EE%D4%19J%17%B4%C3E%FC%BC%AC%A3%02%9D+4%E15%B6%F3%A41%1F%E5; _pdr_internal=GA1.2.929026208.1548105347; _scid=af54eec9-6be3-4fe8-a6f6-18ce38c6811a; EMAGROSESSID=6fc43dc40c21bb0992188079ed7ca027; site_version_11=not_mobile; eab152=a; _gcl_au=1.1.644183029.1584716724; user_remember=%DB%11b%C5dy%B9%BA%A4%928%CA%A9%3D%ECl%9C%A5%24%06%1F%5B%21%280%D9%10%3A%0E_kv3%29%15%1A%FBSB%A6KG%C9%7D%40%C7p%B4%D7%C6%1B%84%3A%CB%F1%8B%B1%5E%DE%F8%96%29%7D%E4%0D7%89%962Kn%E61%09%B1%CB%1Cd%8E%B4%BC%90%17%24%8E%E4%DF%FF%91%EAO%B4%D1%F5%FB%81%94%5Dn%7C%99%60%95%D6%A9%8Aq%0D-%EE%E4%60; sapi-token=eyJ1c2VyX2lkIjoyODA2Nzk2NjQ3LCJ1c2VyX2tleSI6Inc1c1JZc09GWkhuQ3VjSzZ3NUhDc0h4c0swSENpc080SWNPRHc3Qm1lc0tpQ2pSdHdvSERnY09pSDhLNEtzS1dFOEsrUnNLYXc1ekNoY0tcL3c2WENoc0tqQU1LU0hIUUR3cDdDaFNcL0N0TU9YS2NLS0Y4SzF3b1wvRG5WekR2QkhDaE1PaGU4T2VNbXZEbG1kcU9pWXpZY0tHS1JVQnc3XC9DaFE9PSIsImxhbmdfY29kZV9rZXkiOiJ3NXNSWXNPRlpIbkN1Y0s2dzVIQ3NIeHNLMEhDaXNPNFo4S213b1hEaXNPNHc2MHh3NGZDcFhSQnc2WENrUWpEdU1Lenc3ckRuTUs0T01PSkowbkR2Y09zSmNPOHdxUTZ3NU5Fd3JMRHZrSXF3cm5EbThPWnc2akNyY09hSkVyQ21zT0d3cjBXdzdrbXc2a1R3cHJDa1FBbE9EWlB3ckViQlIxY3c3dz0iLCJ1dWlkIjoiMTU2MDUwNjM3Ny0zMzA4NTAwMDUtNzQ1MTkuMDM4In0%3D; EMAG_VIEW=not_mobile; sk_t_undefined=on; profile_token=pftk_4046314096834718785; sk_t_skin_ziua_emag_teasing_=2; sk_c_undefined=3; _rsv=2; _rscd=1; _rsdc=2; eab170=a; _derived_epik=dj0yJnU9bklDSEhMU3JUVHdJQ0ZjNl8yNTlBNW53VHVkTlNSZEYmbj0yOGctTXo3Q09WRllGTUVOYmxPZ1NnJm09NyZ0PUFBQUFBRjUxSE5V; ga_view_id=1584733432-517.190-775797468'
#     cookie = SimpleCookie()
#     cookie.load(cookie_string)

#     cookies = {}

#     for key, morsel in cookie.items():
#         cookies[key] = morsel.value
#     # print(cookies)
#     # print(cookie.items())
#     return cookies
# # cookie_parser()

# def parse_new_url(url, url_nr):
#     url_parsed = urlparse(url)
#     # print(url_parsed.query)
#     query_string = parse_qs(url_parsed.query)
#     # print(type(query_string))
#     query_string['url'] = '/telefoane-mobile/p{}'.format(url_nr)+'/c'
#     # print(query_string)
#     encoded_qs = urlencode(query_string, doseq=1)
#     new_url = f"'https://www.emag.ro/search-by-url?{encoded_qs}"
#     # print(new_url)
#     return new_url
# parse_new_url(URL, 10)