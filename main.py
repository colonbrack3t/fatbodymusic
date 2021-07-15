
import update_video_metadata, requests, json

def main():
    singles_number_one, list_of_songs = get_charts_number_ones()
    print(singles_number_one, list_of_songs)
    update_video_metadata.update_videos('WxYGqqlbifk',singles_number_one + ' (COVER)',' '.join(list_of_songs),'')



# return (singles_number_one, [list of all number ones])
def get_charts_number_ones():
    r =requests.get('https://www.officialcharts.com/Umbraco/Api/ChartsApi/GetMiniCharts/')
    j = json.loads(r.content)
    singles_number_one = ''
    list_of_songs = []
    for charts in j['footer']:
        for songs in charts['positions']:
            if songs['position'] == 1:
                if charts['chart']['Name'] == 'Singles':
                    singles_number_one = songs['product_name'] + ' - ' + songs['artist_name']
                list_of_songs.append(songs['product_name'] + ' - ' + songs['artist_name'])
    return (singles_number_one, list_of_songs)  
main()  