
from deco import register
from api import API

class AwemeSDK:

    def __init__(self,token,host):
        self.host = host.rstrip('/')
        self.token = token

    @register(API.UserInfo)
    def GetUserInfo(self,uid):
        '''
        获取用户信息
        :param uid:用户user id
        '''
        return {
            'token':self.token,
            'uid':uid
        }

    @register(API.UserLiveInfo)
    def GetUserLiveInfo(self, uid):
        '''
        获取直播用户信息
        :param uid: 用户user id
        '''
        return {
            'token': self.token,
            'uid': uid
        }

    @register(API.UserPosts)
    def GetUserPosts(self, uid, cursor=0):
        '''
        获取用户发布的视频作品
        :param uid: 用户user id
        :param cursor: 翻页游标，根据返回结果的max_cursor进行翻页操作，初始值为0
        '''
        return {
            'token': self.token,
            'uid': uid,
            'cursor': cursor,
        }

    @register(API.UserFavourites)
    def GetUserFavourites(self, uid, cursor=0):
        '''
        获取用户点赞过的视频
        :param uid: 用户user id
        :param cursor: 翻页游标，根据返回结果的max_cursor进行翻页操作，初始值为0
        '''
        return {
            'token': self.token,
            'uid': uid,
            'cursor': cursor,
        }

    @register(API.UserPromotions)
    def GetUserPromotions(self, uid, cursor=0):
        '''
        获取用户商品橱窗
        :param uid:用户user id
        :param cursor:翻页游标，默认0
        '''
        return {
            'token': self.token,
            'uid': uid,
            'cursor': cursor,
        }

    @register(API.VideoComments)
    def GetVideoComments(self, aweme_id, cursor=0):
        '''
        获取视频评论
        :param aweme_id:视频id
        :param cursor:翻页游标，默认0，根据返回结果的cursor进行翻页
        '''
        return {
            'token': self.token,
            'aweme_id': aweme_id,
            'cursor': cursor,
        }

    @register(API.VideoDetail)
    def GetVideoDetail(self,aweme_id):
        '''
        获取视频详情
        :param aweme_id:视频的id
        '''
        return {
            'token': self.token,
            'aweme_id': aweme_id,
        }

    @register(API.VideoPromotions)
    def GetVideoPromotions(self, aweme_id):
        '''
        获取某个视频的带货商品信息
        :param aweme_id:视频id
        '''
        return {
            'token': self.token,
            'aweme_id': aweme_id,
        }

    @register(API.VideoCommentReplies)
    def GetVideoCommentReplies(self, aweme_id,cid,cursor=0):
        '''
        获取视频评论的子评论
        :param aweme_id: 视频id
        :param cid: 评论id
        :param cursor: 子评论列表翻页游标，适用于子评论过多的情况下
        '''
        return {
            'token': self.token,
            'aweme_id': aweme_id,
            'cid':cid,
            'cursor':cursor
        }

    @register(API.ChallengeDetail)
    def GetChallengeDetail(self, challenge_id):
        '''
        获取话题（challenge）详情
        :param challenge_id:话题id
        '''
        return {
            'token': self.token,
            'cid': challenge_id
        }

    @register(API.ChallengeVideos)
    def GetChallengeVideos(self, challenge_id,cursor=0):
        '''
        获取话题（challenge）下的视频
        :param challenge_id:话题id
        :param cursor:翻页游标，根据结果返回的cursor进行翻页操作，初始值为0
        '''
        return {
            'token': self.token,
            'cid': challenge_id,
            'cursor':cursor,
        }

    @register(API.PoiDetail)
    def GetPoiDetail(self, poi_id):
        '''
        获取地点（poi）详情
        :param poi_id: 地点id
        '''
        return {
            'token': self.token,
            'poi_id': poi_id
        }

    @register(API.PoiVideos)
    def GetPoiVideos(self, poi_id,cursor=0):
        '''
        获取地点（poi）下的视频
        :param poi_id: 地点id
        :param cursor: 翻页游标，根据结果返回的cursor进行翻页操作，初始值为0
        '''
        return {
            'token': self.token,
            'poi_id': poi_id,
            'cursor':cursor
        }

    @register(API.PromotionsVideosFeed)
    def GetPromotionVideosFeed(self, page=1):
        '''
        带货视频推荐流
        :param page:页数索引
        '''
        return {
            'token': self.token,
            'page': page,
        }

    @register(API.PromotionInfo)
    def GetPromotionInfo(self,promotion_id):
        '''
        获取某样带货商品的信息
        :param promotion_id: 商品id
        '''
        return {
            'token': self.token,
            'promotion_id': promotion_id,
        }

    @register(API.PromotionSameVideos)
    def GetPromotionSameVideos(self, promotion_id):
        '''
        同款商品带货视频推荐
        :param promotion_id:商品id
        '''
        return {
            'token': self.token,
            'promotion_id': promotion_id,
        }

    @register(API.LiveRoomChat)
    def GetLiveRoomChats(self,room_id):
        '''
        获取抖音直播间弹幕/进入直播间观众/刷礼物/关注主播 信息
        :param room_id:直播间id
        '''
        return {
            'token':self.token,
            'room_id':room_id
        }

    @register(API.LiveRoomPromotions)
    def GetLiveRoomPromotions(self,room_id):
        '''
        获取抖音直播间带货商品信息
        :param room_id:直播间id
        '''
        return {
            'token':self.token,
            'room_id':room_id
        }

    @register(API.LiveRoomInfo)
    def GetLiveRoomInfo(self,room_id):
        '''
        获取抖音直播间信息
        :param room_id:直播间id
        '''
        return {
            'token':self.token,
            'room_id':room_id
        }

    @register(API.LiveRoomCheck)
    def GetLiveRoomStatus(self,room_id):
        '''
        查询直播间是否开播
        :param room_id:直播间id
        '''
        return {
            'token':self.token,
            'room_ids':room_id
        }

    @register(API.RealStarBoard)
    def RealStarBoard(self):
        '''
        实时明星爱DOU榜
        '''
        return {
            'token': self.token,
        }

    @register(API.RealHotBoard)
    def RealHotBoard(self):
        '''
        实时热点榜
        '''
        return {
            'token': self.token,
        }

    @register(API.RealGoodsBoard)
    def RealGoodsBoard(self):
        '''
        实时好物榜
        '''
        return {
            'token': self.token,
        }

    @register(API.RealHotVideos)
    def RealHotVideos(self):
        '''
        最热视频榜单
        '''
        return {
            'token': self.token,
        }

    @register(API.RealHotTags)
    def RealHotChallenges(self):
        '''
        热门话题推荐
        '''
        return {
            'token': self.token,
        }

    @register(API.RealBrandBoard)
    def RealBrandBoard(self,category_id,start_date=None):
        '''
        实时品牌榜
        :param category_id: 品牌类别id，可以从品牌类别接口获取，一次即可
        :param start_date:开始日期，可用于抓取历史榜单数据，默认空
        '''
        return {
            'token': self.token,
            'category':category_id,
            'start_date':start_date
        }

    @register(API.RealBrandCates)
    def BrandCategories(self):
        '''
        品牌类别接口
        '''
        return {
            'token': self.token,
        }

    @register(API.RealBrandDetail)
    def BrandDetail(self,category_id,brand_id):
        '''
        热榜品牌详情
        :param category_id:品牌类别id，可以从品牌类别接口获取，一次即可
        :param brand_id:品牌id
        '''
        return {
            'token': self.token,
            'category': category_id,
            'brand_id':brand_id
        }

    @register(API.SearchUsers)
    def SearchUsers(self,keyword,cursor=0):
        '''
        关键词搜索用户
        :param keyword:搜索关键词
        :param cursor:翻页游标，初始为0，根据返回的cursor值进行翻页
        '''
        return {
            'token': self.token,
            'keyword': keyword,
            'cursor':cursor
        }

    @register(API.SearchVideos)
    def SearchVideos(self,keyword,cursor=0):
        '''
        关键词搜索视频
        :param keyword:搜索关键词
        :param cursor:翻页游标，初始为0，根据返回的cursor值进行翻页
        '''
        return {
            'token': self.token,
            'keyword': keyword,
            'cursor':cursor
        }

