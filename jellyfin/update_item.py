class UpdateItem(object):
    def __init__(self):
        self.Id = ""
        self.Name = ""
        self.OriginalTitle = ""
        self.ForcedSortName = ""
        self.CommunityRating = ""
        self.CriticRating = ""
        self.IndexNumber = None
        self.AirsBeforeSeasonNumber = ""
        self.AirsAfterSeasonNumber = ""
        self.AirsBeforeEpisodeNumber = ""
        self.ParentIndexNumber = None
        self.DisplayOrder = ""
        self.Album = ""
        self.AlbumArtists = []
        self.ArtistItems = []
        self.Overview = ""
        self.Status = ""
        self.AirDays = []
        self.AirTime = ""
        self.Genres = []
        self.Tags = []
        self.Studios = []
        self.PremiereDate = ""
        self.DateCreated = ""
        self.EndDate = None
        self.ProductionYear = ""
        self.AspectRatio = ""
        self.Video3DFormat = ""
        self.OfficialRating = ""
        self.CustomRating = ""
        self.People = []
        self.LockData = False
        self.LockedFields = []
        self.ProviderIds = {}
        self.PreferredMetadataLanguage = ""
        self.PreferredMetadataCountryCode = ""
        self.RunTimeTicks = None
        self.Taglines = []

    def __set_id(self, item_id):
        self.Id = item_id

    def __set_name(self, name):
        self.Name = name

    def __set_original_title(self, original_title):
        self.OriginalTitle = original_title

    def __set_forced_sort_name(self, forced_sort_name):
        self.ForcedSortName = forced_sort_name

    def __set_community_rating(self, metadata):
        if 'CommunityRating' in metadata:
            self.CommunityRating = metadata['CommunityRating']

    def __set_overview(self, overview):
        self.Overview = overview

    def __set_genres(self, genres):
        self.Genres = genres

    def __set_studios(self, studios):
        self.Studios = studios
        # for studio in studios:
        #     self.Studios.append({'Name': studio['Name']})

    def __set_premiere_date(self, premiere_date):
        self.PremiereDate = premiere_date

    def __set_date_created(self, date_created):
        self.DateCreated = date_created

    def __set_production_year(self, production_year):
        self.ProductionYear = production_year

    def __set_official_rating(self, metadata):
        if 'OfficialRating' in metadata:
            self.OfficialRating = metadata['OfficialRating']

    def __set_people(self, people):
        self.People = people

    def __set_provider_ids(self, provider_ids):
        self.ProviderIds = provider_ids

    def set_metadata(self, metadata):
        self.__set_id(metadata['Id'])
        self.__set_name(metadata['Name'])
        self.__set_original_title(metadata['OriginalTitle'])
        self.__set_forced_sort_name(metadata['ForcedSortName'])
        self.__set_community_rating(metadata)
        self.__set_overview(metadata['Overview'])
        self.__set_genres(metadata['Genres'])
        self.__set_studios(metadata['Studios'])
        self.__set_premiere_date(metadata['PremiereDate'])
        self.__set_date_created(metadata['DateCreated'])
        self.__set_production_year(metadata['ProductionYear'])
        self.__set_official_rating(metadata)
        self.__set_people(metadata['People'])
        self.__set_provider_ids(metadata['ProviderIds'])
