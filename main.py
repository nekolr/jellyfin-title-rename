from jellyfin.client import JellyfinClient
from jellyfin.update_item import UpdateItem
from peashooter.client import PeashooterClient

if __name__ == "__main__":
    peashooterClient = PeashooterClient()
    series_list = peashooterClient.get_series_list()

    series_dic = dict()
    for series in series_list:
        series_dic[series['originalName']] = series['name']

    jellyfinClient = JellyfinClient()
    jellyfinClient.print_version()
    items = jellyfinClient.get_items()
    for item in items:
        userLibraryItem = jellyfinClient.get_user_library_item(item['Id'])
        original_title = userLibraryItem['Name']
        if original_title in series_dic:
            chinese_title = series_dic[original_title]
            userLibraryItem['OriginalTitle'] = original_title
            userLibraryItem['Name'] = chinese_title
            userLibraryItem['ForcedSortName'] = chinese_title

            updateItem = UpdateItem()
            updateItem.set_metadata(userLibraryItem)
            status = jellyfinClient.update_item(updateItem)
            print(status)
