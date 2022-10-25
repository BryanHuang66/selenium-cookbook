+ Selenium自动化环境搭建
    + 详解整套配置  
        + python
        + selenium
        + chrome + driver
    + Docker完成环境搭建
+ Chrome Driver Options常用属性即方法
    + 导入
        + from selenium.webdriver.chrome.options import  Options
        + options = Options()
    + 设置 chrome 二进制文件位置 (binary_location)
        + options.binary_location = '/usr/bin/google-chrome'
    + 添加启动参数 (add_argument)，参数之间不能用空格
        + headless 无界面模式
        + user-agent  模拟移动设备
        + blink-settings=imagesEnabled=false 设置图片不加载
        + proxy-server=http://120.194.55.139:6969 添加代理
        + incognito 进入隐私模式
        + auto-open-devtools-for-tabs 自动打开开发者工具
        + window-size=300,600  设置窗口大小
        + window-position=120,0  设置窗口位置
        + disable-gpu  禁止gpu
        + start-fullscreen  全屏启动
        + kiosk 全屏启动，无地址栏
        + debugger_address 调试路径
        + ...  https://peter.sh/experiments/chromium-command-line-switches/
    + 添加扩展应用 (add_extension, add_encoded_extension)
    + 添加实验性质的设置参数 (add_experimental_option)
+ Selenium元素查找
    + Selenium的元素查找函数
        find_element & find_elements
    + 简单定位（具有较大的局限性）
        + 使用id属性定位
            + driver.find_element(By.ID,"kw")
        + 使用class_name属性定位
             + driver.find_elements(By.CLASS_NAME, "mnav.c-font-normal.c-color-t")
        + 使用name属性定位
            + driver.find_element(By.NAME,"wd")
        + 使用Link Text链接文本定位
            + driver.find_element(By.LINK_TEXT,"新闻")
        + 使用Partial Link Text部分链接文本定位
            + driver.find_element(By.PARTIAL_LINK_TEXT,"新")
        + 使用 tag 标签定位
            + driver.find_element(By.TAG_NAME ,"input")
    + 高级定位
        + Xpath定位
            + 概念
                + XPath是XML路径语言，是一种查询语言，使用路径表达式浏览XML文档中的元素和属性。
            + 详解
                + 描述层级
                    + 以"//"开头
                    + 描述儿子层级：使用"//"或者"/"，其中"//"开头代表的是相对路径，使用"/+ child::element"
                        + driver.find_element(By.XPATH,"//body/div[1]/div[1]/div[3]/a[1]")
                    + 描述子孙层级：使用"//" 或者 "/descendant::element"
                        + driver.find_element(By.XPATH,"//body//div[3]/a[1]")
                    + 描述兄弟层级：使用 "/following-sibling::element"或者"/+ preceding-sibling::element"
                        + driver.find_element(By.XPATH,"//body//div[3]/a[1]/following-sibling::a")
                        + ⚠️ 区别于CSS_selector，Xpath可以定位到前面的元素“preceding-sibling::element”
                    + 描述父爷层级：使用".."，"/parent::element" 或者 "/+ ancestor::element" 
                        + driver.find_element(By.XPATH,"//body//div[3]/a[2]/../a[2]")
                    + 使用“preceding::element”或者“following::element”描述当前元素+ 节点标签之前的所有节点或者当前元素节点标签之后的所有节点
                + 描述属性值
                    + driver.find_element(By.XPATH,"//body//div[3]/a[@href='http://news.baidu.com']")
                    + 逻辑元素
                        + Xpath可以使用 ‘and’ 或者 ‘or’ 连接两个属性
                            + driver.find_element(By.XPATH,"//body//div[3]/a[@target='_blank' and @class='mnav c-font-normal c-color-t'][3] ")
                        + ^= 匹配前缀，$= 匹配后缀，*= 包含某个字符串
                + Xpath Text()方法
                    + 使用文本内容完全匹配
                        + driver.find_element(By.XPATH,"//body//div[3]/a[text()='新闻']")
                + Xpath Starts-with()方法
                    + driver.find_element(By.XPATH,"//body//div[3]/a[starts-with(text(),'新')]")
                + Xpath Contains()方法
                    + 文本部分匹配-包含：//标签名[contains(text(),部分文本内容)]
                        + driver.find_element(By.XPATH,"//body//div[3]/a[contains(text(),'新')]")
        + CSS Selector定位
            + 概念
                + CSS (Cascading Style Sheets)是一种样式表语言，是所有浏览器内置的，用于描述以HTML或XML编写的文档的外观和样式。CSS Selector用于选择样式化的元素。
            + 详解
                + 根据子元素与后代元素定位
                    + 如果 元素2 是 元素1 的 直接子元素， 使用 ">" 作连接符
                        + driver.find_element(By.CSS_SELECTOR ,"form>div>input")
                    + 如果元素2是元素1的后代元素（后代元素包含子元素），通过空格隔开元素即可
                        + driver.find_element(By.CSS_SELECTOR ,"form input")
                + 弟弟节点
                    + 找一个弟弟：element + element
                    + 找所有弟弟：element ~ element
                        + driver.find_element(By.CSS_SELECTOR,'body>div div[id="s-top-left"]>a+a')
                + 属性定位
                    + 支持通过任何属性来选择元素，语法是用一个方括号 []
                        + driver.find_element(By.CSS_SELECTOR,'body>div div[id="s-top-left"]>a[href="http://tieba.baidu.com/"]')
                    + 逻辑元素
                        + ^= 匹配前缀
                        + $= 匹配后缀
                        + *= 包含某个字符串
                         + And
                           + driver.find_element(By.CSS_SELECTOR,'body>div div[id="s-top-left"]>a[href*="//map."]')
                + 根据次序选择子节点
                    + 父元素的第n个子节点
                        + 使用 nth-child(n)，可以指定选择父元素的第几个子节点。
                    + 父元素的倒数第n个子节点
                        + 使用 nth-last-child(n)，可以倒过来，选择的是父元素的倒数第几个子节点。
                    + 父元素的第几个某类型的子节点
                      + 使用 nth-of-type(n)，可以指定选择的元素是父元素的第几个某类型的子节点。
                    + 父元素的倒数第几个某类型的子节点
                         + 使用 nth-last-of-type(n)，可以倒过来， 选择父元素的倒数第几个某类型的子节点。
                    + 奇数节点和偶数节点
                        + 如果要选择的是父元素的偶数节点，使用 nth-child(even)
                        + 如果要选择的是父元素的奇数节点，使用 nth-child(odd)
                        + 如果要选择的是父元素的某类型偶数节点，使用 nth-of-type(even)
                    + driver.find_element(By.CSS_SELECTOR,'body>div div[id="s-top-left"]>a:nth-of-type(even)')
        + VS
            + XPath通过遍历的方式从XML文档中选择节点，CSS Selector是一种匹配模式定位，因此CSS Selector比 XPath 执行效率更高。
            + Xpath可以通过文本来定位，而CSS Selector不能。
            + Xpath可以通过子节点来定位父节点，CSS Selector是前向的，不能利用子节点定位父节点。
            + CSS Selector语法相比Xpath更加简洁