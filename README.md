# 售前商机跟踪 - APK 构建指南

## 📦 下载项目

下载 `presales-tracker-apk.tar.gz` 并解压到一个目录，例如：
```
C:\projects\presales-tracker-apk\
```

## 🛠️ 环境准备

### 1. 安装 Node.js（如果没有）
- 下载地址：https://nodejs.org/
- 选择 LTS 版本（推荐 v18 或更高）
- 安装后打开命令提示符（CMD）验证：
```
node --version
npm --version
```

### 2. 安装 Java JDK 17（必需）
- 下载地址：https://adoptium.net/temurin/releases/?version=17
- 选择 Windows x64 JDK
- 安装并设置环境变量：
  - 新建 `JAVA_HOME` = `C:\Program Files\Eclipse Adoptium\jdk-17.x.x.x-hotspot`（根据实际路径）
  - 在 `Path` 中添加 `%JAVA_HOME%\bin`

### 3. 安装 Android SDK（构建 APK 必需）
- 下载 Android Studio：https://developer.android.com/studio
- 安装时选择 "Custom" 并勾选：
  - Android SDK
  - Android SDK Platform-tools
  - Android SDK Build-tools
- 设置环境变量：
  - 新建 `ANDROID_HOME` = `C:\Users\你的用户名\AppData\Local\Android\Sdk`
  - 在 `Path` 中添加 `%ANDROID_HOME%\platform-tools`

## 📲 构建 APK

1. 打开命令提示符，进入项目目录：
```
cd C:\projects\presales-tracker-apk
```

2. 安装依赖：
```
npm install
```

3. 同步 Capacitor：
```
npm run build
```

4. 构建 APK：
```
cd android
.\gradlew assembleDebug
```

5. APK 文件位置：
```
android\app\build\outputs\apk\debug\app-debug.apk
```

## 📱 安装到手机

1. 用数据线连接手机到电脑
2. 开启手机的 "USB 调试"（在设置 → 开发者选项中）
3. 复制 APK 到手机，或使用以下命令安装：
```
adb install android\app\build\outputs\apk\debug\app-debug.apk
```

## 💡 提示

- 如果 gradlew 命令下载依赖很慢，可以先设置国内镜像
- 华为手机可能需要开启 "USB 调试（安全设置）" 才能安装 APK
