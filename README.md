# effective-broccoli
## Lab1
### task 1
```python
print("hello world")
(shot.png.png)[screenshot]!
import subprocess

# 1. إضافة الملفات المعدلة (مثلاً README.md)
subprocess.run(["git", "add", "README.md"])

# 2. عمل commit
commit_message = "تحديث ملف README"
subprocess.run(["git", "commit", "-m", commit_message])

# 3. رفع التغييرات
subprocess.run(["git", "push", "origin", "main"])  # غيّر "main" إذا عندك "master"