import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# from .models import *

posts1 = [{'content' : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."},
         {'content' : "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"},
         {'content' : "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?"},
         {'content' : "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat."},
         {'content' : "who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains."},
         {'content' : "Nulla eleifend, sem sit amet auctor ullamcorper, turpis nisi auctor felis, vitae rutrum enim felis quis sapien. In venenatis felis metus, vel malesuada eros pulvinar ac. Etiam hendrerit fringilla mi eget porttitor. Ut dapibus lorem eu semper facilisis. Ut hendrerit metus a ornare faucibus. Pellentesque dignissim arcu quis tellus hendrerit suscipit. Fusce id varius sem, quis consequat diam. In hac habitasse platea dictumst."},
         {'content' : "Proin rutrum sit amet augue laoreet placerat. Praesent sagittis at mi vitae molestie. In hendrerit augue aliquet, lacinia odio sed, aliquam quam. Vestibulum placerat laoreet congue. Nullam vehicula risus quis nisi lacinia, at rutrum ligula sagittis. Aenean eget sapien congue odio convallis finibus. Nam tempor efficitur malesuada. Cras ullamcorper elit nec nisi tempus tincidunt."},
         {'content' : "Donec tempus vestibulum odio sit amet maximus. Pellentesque at arcu molestie nulla faucibus volutpat pulvinar sit amet ex. Aliquam mattis neque turpis, eu mattis enim finibus sit amet. Phasellus vitae sagittis tortor, quis vulputate tellus. Pellentesque non efficitur nibh. Cras commodo erat sit amet ante varius faucibus. Phasellus euismod at neque quis placerat. Proin efficitur dolor cursus congue venenatis. Maecenas ut lacus a ligula scelerisque porta non ut nunc. Donec auctor porttitor erat. Suspendisse cursus ornare urna, pharetra luctus purus vestibulum eu."},
         {'content' : "Cras vel ex sit amet nulla varius finibus. Maecenas et libero lorem. Mauris tincidunt erat sodales, sodales lectus a, consequat purus. Duis semper ligula risus, sed convallis erat condimentum a. Donec lacus magna, commodo laoreet lacinia feugiat, scelerisque a dolor. Ut dictum magna tempus sapien egestas, quis aliquam orci viverra. Aliquam rhoncus nibh non pellentesque elementum. Praesent massa justo, elementum nec iaculis non, cursus et tortor. Mauris accumsan euismod feugiat. Mauris in dui nec elit fringilla finibus tincidunt eu lacus. Sed hendrerit metus ac erat ornare, eget elementum massa luctus. Morbi quis faucibus ligula. Duis faucibus convallis magna nec sodales. Phasellus non pretium mauris. Sed fermentum varius augue."},
         ]

posts2 = [{'content' : "Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Praesent non metus lacus. Phasellus tellus ipsum, dignissim nec ornare semper, hendrerit ut leo. Integer ultrices ipsum at turpis volutpat, ac pellentesque turpis lacinia. Vestibulum sapien nulla, maximus nec dolor sed, ullamcorper malesuada neque. Sed tempor risus lectus, scelerisque cursus nulla fermentum vitae. Proin ultrices nisl non placerat malesuada. Aliquam dapibus eros a dui iaculis vulputate. Suspendisse sit amet elit venenatis, iaculis quam nec, mollis nulla."},
         {'content' : "Sed eget dolor est. Suspendisse potenti. Lorem ipsum dolor sit amet, consectetur adipiscing elit. In condimentum interdum mauris, condimentum mattis nisi auctor tempus. Duis urna ipsum, molestie interdum dictum sit amet, consectetur vel risus. Nunc vel feugiat quam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc volutpat placerat nulla, eget porttitor augue sodales eget. Praesent non euismod eros. Nunc et justo malesuada, feugiat est fermentum, congue odio. Integer sagittis eget justo eget malesuada. Curabitur sed posuere elit. Phasellus in mattis orci."},
         ]


posts3 = [{'content' : "Proin vel dolor blandit nulla viverra condimentum. Fusce mi ante, fermentum a neque et, fringilla placerat nunc. Quisque sed lectus ac orci accumsan elementum. Aliquam eu ex enim. Curabitur lobortis neque eget arcu eleifend elementum. Ut mollis, tellus in aliquet placerat, enim nisi scelerisque felis, eu vestibulum ex diam sit amet leo. Morbi vitae rutrum diam, eu venenatis justo. Donec at posuere nibh. In hac habitasse platea dictumst. Etiam auctor erat nec nisi dictum, at pellentesque ante dignissim. Curabitur lacinia, metus eu rhoncus facilisis, lorem enim malesuada est, at elementum nulla tellus sit amet velit. Sed placerat commodo erat, vitae lobortis arcu faucibus at."},
         {'content' : "In pretium dui ipsum, sed lacinia turpis venenatis vitae. Ut pulvinar tortor sit amet ante eleifend volutpat. Pellentesque ut magna urna. Mauris dictum orci purus, ut tempus nisl finibus eu. Nunc ullamcorper suscipit lobortis. Etiam vitae quam laoreet, aliquam sapien in, sollicitudin metus. Proin sed erat porta, vestibulum tellus id, pulvinar lorem. Suspendisse ac laoreet eros, dapibus laoreet nibh. Phasellus eleifend sed tellus in sodales. Donec cursus consectetur sapien."},
         {'content' : "Interdum et malesuada fames ac ante ipsum primis in faucibus."},
         ]


class NetworkSeleniumTestCase(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        
    def test(self):
        driver = self.driver
        url = "http://127.0.0.1:8000"
        
        # login
        driver.get(url)
        time.sleep(2)
        a = driver.find_element(By.CSS_SELECTOR,"a.LogIn_Link")
        a.click()
        driver.implicitly_wait(4)
        NetworkSeleniumTestCase.login(self,"zahra","123")
        
        
        # new posts
        NetworkSeleniumTestCase.addPost(self, posts1)

        time.sleep(2)    
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)    
        driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
        time.sleep(2)    
        
        NetworkSeleniumTestCase.addPost(self,posts2)

            
        time.sleep(2)    
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")    
        time.sleep(2)    
        driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
        time.sleep(2)    
        
        # login as another user   
        a = driver.find_element(By.CSS_SELECTOR,"a.LogOut_Link")
        a.click()
        driver.implicitly_wait(4)
        a = driver.find_element(By.CSS_SELECTOR,"a.LogIn_Link")
        a.click()
        driver.implicitly_wait(4)
        NetworkSeleniumTestCase.login(self,"maryam","123")

        
        # *****new posts*****
        NetworkSeleniumTestCase.addPost(self,posts3)

          
       
        
        # ******Pagination******
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        page = driver.find_element(By.CSS_SELECTOR,"a.page-next")
        if(page):
            page.click()
        
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        page = driver.find_element(By.CSS_SELECTOR,"a.page-previous")
        if(page):
            page.click()
        
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        page = driver.find_element(By.CSS_SELECTOR,"a.page-next")
        if(page):
            page.click()
        time.sleep(2)
        
        # ******Profile Page******
        a = driver.find_element(By.CSS_SELECTOR,".card-header:first-child > a")
        a.click()
        driver.implicitly_wait(4)
        time.sleep(2)
        
        for i in range(3):
            follow = driver.find_element(By.ID,"follow")
            follow.click()
            time.sleep(2)
       
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        page = driver.find_element(By.CSS_SELECTOR,"a.page-next")
        if(page):
            page.click()
        time.sleep(2)
        
        # ******“Like” and “Unlike”******
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        like = driver.find_element(By.CSS_SELECTOR,"a.card-link")
        for i in range(3):
            like.click()
            time.sleep(1)
       
        
       

        # ******Following******
        a = driver.find_element(By.CSS_SELECTOR,"a.Following-link")
        a.click()
        driver.implicitly_wait(2)
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        page = driver.find_element(By.CSS_SELECTOR,"a.page-next")
        if(page):
            page.click()
        time.sleep(2)
        
        
        # *****all posts*****
        a = driver.find_element(By.CSS_SELECTOR,"a.AllPosts-link")
        a.click()
        driver.implicitly_wait(4)
        time.sleep(2)
        
        
        # ******Edit Post******
        edit = driver.find_element(By.CSS_SELECTOR,"a.edit_post")
        edit.click()
        time.sleep(2)
        content = driver.find_element(By.NAME,"content")
        content.click()
        driver.implicitly_wait(2)
        content.clear()
        content.send_keys("Edit Interdum et malesuada fames ac ante ipsum primis in faucibus.")
        time.sleep(2)
        post = driver.find_element(By.ID,"save_editPost")
        post.click()
        time.sleep(2)
        
     
      # ******Profile Page******
        a = driver.find_element(By.CSS_SELECTOR,".card-header:first-child > a")
        a.click()
        driver.implicitly_wait(4)
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        like = driver.find_element(By.CSS_SELECTOR,"a.card-link:last-child")
        like.click()
        time.sleep(2)
        driver.refresh()
        driver.implicitly_wait(4)
     
        
    def login(self,_username,_password):
        driver = self.driver
        username = driver.find_element(By.NAME,"username")
        password = driver.find_element(By.NAME,"password")
        login = driver.find_element(By.ID,"login")
        username.click()
        username.send_keys(_username)
        password.click()
        password.send_keys(_password)
        login.click()
        driver.implicitly_wait(2)
        
    def addPost(self,posts):
          driver = self.driver
          for item in posts:
            content = driver.find_element(By.NAME,"content")
            content.click()
            content.send_keys(item["content"])
            post = driver.find_element(By.ID,"save_createPost")
            post.click()

    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
        
     
# Create your tests here.
# class NetworkTestCase(TestCase):

#     def setUp(self):

#         # Create User1.
#         username = "hamide"
#         email = "hamide@gmail.com"
#         password = "123"
#         user1 = User.objects.create_user(username, email, password)
        
#         # Create User2.
#         username = "zahra"
#         email = "zahra@gmail.com"
#         password = "123456"
#         user2 = User.objects.create_user(username, email, password)
        
#         # Create Posts.
#         post1 = Post.objects.create(content="AAA", user=user1)
#         post2 = Post.objects.create(content="BBB", user=user1)
#         post3 = Post.objects.create(content="CCC", user=user1)
#         post4 = Post.objects.create(content="DDD", user=user2)
        
        
#        # Create Follow.
#         follow1 = Follow.objects.create(user=user1)
#         follow1.follower.add(user2)
#         follow2 = Follow.objects.create(user=user2)
#         follow2.following.add(user1)


#     def test_posts_count(self):
#         count = Post.objects.count()
#         self.assertEqual(count, 4)
        
#     def test_follows_count(self):
#         count = Follow.objects.count()
#         self.assertEqual(count, 2)
#         user1 = User.objects.get(username="hamide")
#         followers_count = user1.followings.count()
#         followings_count = user1.followers.count()
#         self.assertEqual(followers_count, 1)
#         self.assertEqual(followings_count, 0)
        
#         user2 = User.objects.get(username="zahra")
#         followers_count = user2.followings.count()
#         followings_count = user2.followers.count()
#         self.assertEqual(followers_count, 0)
#         self.assertEqual(followings_count, 1)
        
     
       
        
  


    
