# LuxBoat Due Date Calculator - Student Guide

Welcome! This project will teach you how to use Python to solve a real business problem: calculating reliable due dates for manufacturing orders.

## 📚 What You'll Learn

- Basic Python programming
- Statistical analysis (mean, variance, autocorrelation)
- Data visualization
- Building interactive web applications with Streamlit

**No programming experience needed!** This project is designed for complete beginners.

## 🚀 Getting Started

### Option 1: Google Colab (Recommended for Beginners)

1. Go to [Google Colab](https://colab.research.google.com/)
2. Sign in with your Google account
3. Upload the notebook file: `luxboat_student_template.ipynb`
4. Click "Runtime" → "Run all" to start

**Advantages**: 
- No installation required
- Free to use
- Works in any web browser
- Automatic saving to Google Drive

### Option 2: Local Installation

If you want to work on your own computer:

1. **Install Python** (if not already installed):
   - Download from [python.org](https://www.python.org/downloads/)
   - Choose Python 3.8 or later

2. **Install Jupyter**:
   ```bash
   pip install jupyter
   ```

3. **Install required libraries**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Start Jupyter**:
   ```bash
   jupyter notebook
   ```

5. **Open the student template** in your browser

## 📁 Files Included

### For Learning
- `luxboat_student_template.ipynb` - **START HERE!** Complete this notebook first
- `luxboat_complete.ipynb` - Reference solution (check this if you get stuck)
- `INSTRUCTOR_GUIDE.md` - Teaching guide (for your instructor)

### For Streamlit App
- `luxboat_streamlit_app.py` - Interactive web application
- `requirements.txt` - List of Python packages needed

## 🎯 Project Steps

### Step 1: Complete the Notebook (2-3 hours)

Open `luxboat_student_template.ipynb` and work through it section by section.

**What to do in each section:**
1. Read the explanation text carefully
2. Look for cells marked with `TODO`
3. Fill in the missing code
4. Run the cell to check if it works
5. Compare your output with the expected results

**Tips:**
- Read the comments in the code - they explain what each line does!
- If you get an error, read the error message carefully
- Check if you missed any parentheses or quotes
- Make sure your indentation is correct

### Step 2: Run the Streamlit App (1 hour)

After completing the notebook, try the web application:

1. **Install Streamlit** (if not already installed):
   ```bash
   pip install streamlit
   ```

2. **Run the app**:
   ```bash
   streamlit run luxboat_streamlit_app.py
   ```

3. **Explore the features**:
   - Try different confidence levels
   - Upload your own data (CSV format)
   - Look at the visualizations
   - Understand how the calculations work

### Step 3: Customize (Optional Challenge)

Try modifying the Streamlit app:
- Change the colors
- Add a new visualization
- Calculate additional statistics
- Improve the user interface

## 🤔 Common Questions

### "I get an error when I run a cell!"
- Check the error message - it usually tells you what's wrong
- Make sure you ran all the previous cells first
- Check for typos in your code
- Look at the complete notebook for reference

### "What does 'ddof=1' mean?"
- It's a parameter for calculating sample variance (more accurate for estimates)
- Don't worry too much about it - just include it when calculating variance

### "Why can't I just use the average?"
- The average doesn't account for variability (some boats take longer, some faster)
- We need confidence intervals to give reliable promises to customers

### "What if my autocorrelation is different?"
- That's okay! Your results will differ slightly from the example
- The important thing is understanding how to calculate it

### "How do I upload data to the Streamlit app?"
- Your CSV file needs ONE column named "inter_throughput_time"
- Each row should have one number (time in hours)
- See the example in the app's help section

## 📊 Understanding Your Results

After completing the calculations, you should see:

- **Average time**: ~40.5 days (50% chance of completion)
- **Due date with 90% confidence**: ~43 days
- **Safety time**: ~2.5 days (extra buffer for reliability)
- **Autocorrelation**: ~0.38 (moderate positive correlation)

These numbers show that:
1. Simple averages underestimate the time needed
2. Production times are correlated (one delay often leads to another)
3. Adding safety time ensures we deliver on our promises

## 🎓 Learning Checklist

By the end of this project, you should be able to:

- [ ] Import and use Python libraries (numpy, pandas, matplotlib)
- [ ] Work with lists and calculate statistics
- [ ] Create visualizations (histograms, line plots)
- [ ] Understand autocorrelation and why it matters
- [ ] Calculate confidence intervals
- [ ] Write functions with parameters and return values
- [ ] Run a Streamlit web application
- [ ] Upload and process CSV data

## 🆘 Getting Help

1. **Check the complete notebook** (`luxboat_complete.ipynb`) for reference
2. **Read the error messages** - they're helpful!
3. **Ask your classmates** - explaining helps everyone learn
4. **Ask your instructor** - that's what they're there for!
5. **Google the error** - many others have had the same issue

## 🎉 Next Steps

After completing this project:

1. **Experiment**: Try different datasets and confidence levels
2. **Extend**: Add new features to the Streamlit app
3. **Apply**: Think about other problems you could solve this way
4. **Share**: Show your app to friends or family!

## 📖 Additional Resources

### Python Basics
- [Python for Everybody](https://www.py4e.com/) - Free interactive course
- [Real Python Tutorials](https://realpython.com/) - Clear explanations
- [Python Tutor](http://pythontutor.com/) - Visualize code execution

### Statistics
- [Seeing Theory](https://seeing-theory.brown.edu/) - Visual statistics guide
- [StatQuest Videos](https://www.youtube.com/c/joshstarmer) - Fun explanations

### Streamlit
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Gallery](https://streamlit.io/gallery) - Example apps for inspiration

## 🏆 Challenge Yourself

Once you're comfortable with the basics:

1. **Collect real data**: Time yourself doing a repetitive task
2. **Make predictions**: Calculate when you'll finish your homework
3. **Compare methods**: What if we ignored autocorrelation?
4. **Visualize differently**: Create new charts and graphs
5. **Build something new**: Apply these concepts to a different problem

## 💡 Remember

- Programming is about **problem-solving**, not memorization
- **Everyone** makes mistakes - that's how we learn!
- **Error messages** are your friends
- **Comments** in code are there to help you
- **Practice** makes progress (not perfection!)

Good luck and have fun! 🚤

---

**Questions or issues?** 
- Check the `INSTRUCTOR_GUIDE.md` for teaching tips
- Review your class materials
- Ask your instructor during office hours
