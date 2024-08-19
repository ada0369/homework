# Github学习使用笔记  

+ ## 基本操作内容

git clone  

git pull  

git commit and git push

## 1.Git文件状态简介

Git中文件的三种状态： committed（已提交） ， modified（已修改）、staged（已暂存）
committed ： 表示该文件已经被安全地保存在本地数据库中了
modified：表示修改了某个文件，但还没有提交保 存
staged ：表示把已修改的文件放在下次提交时要保存的清单中     

## 2.初次运行Git前的配置  

git config命令用来配置或读取Git的工作环境。
git config --system :配置对所有用户都普遍适用的配置
git config --global :配置对所有用户都普遍适用的配置  

## 3.Git常用命令介绍   

（1） 创建git仓库

从现有目录创建：切换到现有目录， git init
从现有仓库创建： git clone [url网址]

（2） 检查文件状态

git status

（3）添加文件到暂存区域

git add 文件名
git add -A :提交所有文件到暂存区域

（4）提交文件到git目录

将暂存区域提交： git commit -m “文件说明”

（5）移除文件

git rm 文件名
git rm -f 文件名 ：删除暂存区的文件

（6）比较文件修改的差异

git diff

（7）移动文件或者重命名文件

git mv origin_filename rename_filename

（8）查看提交历史

git log

（9）回退到以前的版本

git reset –hard 版本号

（10）添加远程库

创建 SSH key: ssh-keygen –t rsa –C “Your Email”
查看.ssh目录，找到id_rsa和id_rsa.pub两个文件
登录GitHub账户，输入id_rsa.pub公钥
测试是否成功 ssh -T git@github.com
在github上创建一个与本地仓库同名的空仓库
运行命令： git remote add origin git@github.com:用户名/learngit.git  
git push -u origin master： 推送到远程仓库  

## 4、 Git的分支管理  

Git分支简介： Git 中的分支，其实本质上仅仅是个指向 commit 对
象的可变指针
• 创建与合并分支
• 冲突管理和远程分支
• 忽略特殊文件  

## 5、忽略特殊文件  

创建并编写.gitignore文件：输入你想忽略的文件,例如： .obj、 .tmp
• 将.gitignore文件提交到git  



+ ## Github简介

  ### 基本概念

  1、 Repository（仓库）： 用来存放你的项目代码，每个项目对应一
  个仓库。
  2、 Star（收藏） ：即收藏别人的项目，方便查看
  3、 Fork: 复制克隆项目，与所克隆的项目是独立存在的
  4、 Pull Request：发起请求，等待原项目负责人查看，考虑是否合
  并到源仓库中  
  5、 Watch：如果你watch了一个项目，如果以后这个项
  目有更新时可及时接收到通知。
  6、 Issue:发现代码有Bug时，向项目负责人提提案，讨
  论解决问题
  7、 gist:用来粘贴数据（代码）  

  ### 开源项目贡献流程  

  1、 通过新建Issue提交使用问题或者建议给作者
  2、 通过Pull Request Fork 作者项目、对项目进行修改并提交Pull Request、等待作者审核  

  ### 团队合作开发项目

  1、通过 Collaborators   2、 Fork & Pull Request  