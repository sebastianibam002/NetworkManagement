from InstagramController.InstagramPost import InstagramPost
from PostGenerator.PostsOfTheDay import PostsOfTheDay
import pytz
from datetime import datetime

local_tz = pytz.timezone('America/Bogota')
def convert_time_zone(utc_dt):
    colombian_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_tz.normalize(colombian_dt) # .normalize might be unnecessary

"""
When called would post the post with according to the time
"""
def post_with_time():
    time_comp = datetime.utcnow()
    colombian_time = convert_time_zone(time_comp)
    print(colombian_time)
    # create the three posts of the day
    daily_posts = PostsOfTheDay()
    daily_posts.fill_with_information(colombian_time)
    daily_posts.generate_posts(colombian_time)
    ig_poster = InstagramPost()
    ig_poster.location_file_post = daily_posts.get_available_one()
    ig_poster.post(colombian_time)




def main():
    """
    This would be in charge of running on the backgroung posting the different
     posts troughout the day
    """ 
    pass


if __name__ == "__main__":
    post_with_time()