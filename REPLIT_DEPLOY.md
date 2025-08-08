# 🚀 Deploy to Replit

This guide will help you deploy the Redis Semantic Cache Demo to Replit.

## 📋 Quick Deploy Steps

### Method 1: Import from GitHub (Easiest)

1. **Fork or Import**:
   - Go to [replit.com](https://replit.com)
   - Click "Create Repl"
   - Select "Import from GitHub"
   - Enter: `https://github.com/svkmsr6/redis-semantic-cache-demo`
   - Click "Import from GitHub"

### Method 2: Manual Upload

1. **Create New Repl**: 
   - Go to [replit.com](https://replit.com)
   - Click "Create Repl"
   - Choose "Python" template
   - Name it "redis-semantic-cache-demo"

2. **Upload Files**: 
   - Drag and drop all project files
   - Or use Replit's file upload feature

## 🔧 Configuration for Replit

### 1. Environment Variables (Secrets)

**Important**: Set up your environment variables in Replit:

1. Click the "Secrets" tab in your Repl (🔒 icon)
2. Add these secrets:

```
RDS_URI = your_redis_connection_string
OPENAI_API_KEY = your_openai_api_key
```

**Never put these in your code files!**

### 2. Required Files

The following files are configured for Replit:

- `.replit` - Replit configuration
- `replit.nix` - Nix environment setup
- `requirements.txt` - Python dependencies
- `app.py` - Modified for Replit hosting

### 3. Dependencies Installation

Replit will automatically install dependencies from `requirements.txt` when you run the project.

## ▶️ Running the Application

1. **Click "Run"** - Replit will start the Flask application
2. **Open in New Tab** - Click the open-in-new-tab icon when the webview appears
3. **Test the Demo** - Try the different demo modes

## 🌐 Accessing Your App

- **Development**: Available in Replit's webview
- **Public URL**: Replit provides a public URL for sharing
- **Custom Domain**: Available with Replit Pro

## 🔧 Troubleshooting

### Common Issues:

1. **"Module not found" errors**:
   - Check that `requirements.txt` includes all dependencies
   - Click "Packages" and install missing packages manually

2. **Environment variable errors**:
   - Verify Redis URI and OpenAI API key are set in Secrets
   - Check for typos in variable names

3. **Port binding issues**:
   - The app is configured to use Replit's port automatically
   - Don't modify the port settings

4. **Redis connection fails**:
   - Ensure your Redis Cloud instance allows external connections
   - Check if your Redis URI includes the correct protocol (redis:// or rediss://)

5. **OpenAI API errors**:
   - Verify your API key is valid
   - Check your OpenAI account has sufficient credits

### Performance Optimization:

1. **Keep Repl Active**: Replit may sleep inactive repls
2. **Use UptimeRobot**: Set up monitoring to keep your repl awake
3. **Upgrade to Replit Pro**: For better performance and always-on hosting

## 🚀 Deployment Features

### Replit Advantages:
- ✅ **Zero-config deployment**
- ✅ **Automatic HTTPS**
- ✅ **Built-in environment management**
- ✅ **Collaborative editing**
- ✅ **Version control integration**
- ✅ **Public sharing**

### Production Considerations:
- 🔒 **Environment Variables**: Use Replit Secrets for sensitive data
- 📊 **Monitoring**: Set up uptime monitoring
- 🔄 **Auto-restart**: Replit handles application restarts
- 🌍 **Global CDN**: Replit provides global content delivery

## 📱 Mobile Compatibility

The web interface is fully responsive and works on:
- 📱 **Mobile phones**
- 📱 **Tablets** 
- 💻 **Desktop browsers**
- 🖥️ **Large screens**

## 🤝 Sharing Your Deployment

Once deployed, you can:
- Share the public Replit URL
- Embed in websites using Replit's embed feature
- Invite collaborators to edit the code
- Fork the repl for others to customize

## 🔗 Useful Links

- [Replit Documentation](https://docs.replit.com/)
- [Python on Replit](https://docs.replit.com/programming-ide/languages/python)
- [Environment Variables in Replit](https://docs.replit.com/programming-ide/workspace-features/secrets)
- [Custom Domains](https://docs.replit.com/hosting/custom-domains)

---

**Happy Deploying! 🎉**
