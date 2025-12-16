# LuxBoat Due Date Quoting - Instructor Guide

## Overview
This teaching package helps students learn statistical analysis and Python programming through the LuxBoat case study. It's designed for students with **NO prior programming experience**.

## Learning Objectives
By the end of this module, students will be able to:
1. Understand throughput analysis and due date quoting
2. Calculate basic statistics (mean, variance, standard deviation)
3. Understand and calculate autocorrelation
4. Apply the Central Limit Theorem to business problems
5. Write basic Python code with comments
6. Create an interactive web application using Streamlit

## Materials Included

### 1. Complete Working Notebook (`luxboat_complete.ipynb`)
- **Purpose**: Reference solution for instructors and struggling students
- **When to use**: 
  - Show students what they're building toward
  - Help debugging when students are stuck
  - Demonstrate best practices
- **Recommendation**: Share after students complete the template

### 2. Student Template (`luxboat_student_template.ipynb`)
- **Purpose**: Scaffolded learning experience with TODO sections
- **When to use**: Main assignment for students
- **Structure**: 
  - Complete code cells (run as-is)
  - TODO cells (students fill in)
  - Reflection questions at the end
- **Time estimate**: 2-3 hours with guidance

### 3. Streamlit App (`luxboat_streamlit_app.py`)
- **Purpose**: Final project demonstrating real-world application
- **When to use**: After completing the notebook exercises
- **Skills demonstrated**:
  - File uploads and data parsing
  - User interface design
  - Function reusability
  - Data visualization
- **Time estimate**: 1-2 hours with guidance

## Suggested Teaching Sequence

### Week 1: Introduction & Setup (2 hours)
1. **Introduction to the case** (30 min)
   - Read through the LuxBoat case study together
   - Discuss Joseph's problem
   - Explain why simple averages don't work

2. **Google Colab setup** (30 min)
   - Show students how to access Colab
   - Create first notebook
   - Run first Python cell
   - Explain cells vs. scripts

3. **Python basics** (60 min)
   - Variables and assignment
   - Lists and indexing
   - Functions (calling, not writing yet)
   - Reading error messages

**Homework**: Review Python basics, watch intro videos

### Week 2: Statistical Calculations (3 hours)
1. **Working with the template** (2 hours)
   - Distribute `luxboat_student_template.ipynb`
   - Guide students through Steps 1-4
   - Focus on:
     - Understanding code comments
     - Using numpy functions
     - Interpreting outputs
   
2. **Autocorrelation concept** (30 min)
   - Explain with examples
   - Show robot failure scenario
   - Visualize with scatter plots

3. **Complete Steps 5-7** (30 min)
   - Students work on autocorrelation calculation
   - Calculate final due date
   - Discuss results as a class

**Homework**: Complete Steps 8-10 of template

### Week 3: Functions & Streamlit Intro (3 hours)
1. **Review homework** (30 min)
   - Discuss completed templates
   - Address common errors
   - Show complete solution

2. **Introduction to functions** (60 min)
   - Why functions are useful
   - Writing a simple function
   - Parameters and return values
   - Complete Step 10 together

3. **Streamlit basics** (90 min)
   - What is Streamlit?
   - Install Streamlit locally or use Streamlit Cloud
   - Basic structure of a Streamlit app
   - Run the example app together
   - Explore features interactively

**Homework**: Experiment with the Streamlit app

### Week 4: Streamlit Customization (2 hours)
1. **App architecture walkthrough** (60 min)
   - Input methods (sidebar)
   - Tabs for organization
   - Visualization updates
   - Download functionality

2. **Modification exercise** (60 min)
   Students modify the app to:
   - Change colors/styling
   - Add new confidence levels
   - Create additional visualizations
   - Add new features (optional)

**Final Project**: Create a customized version of the Streamlit app

## Teaching Tips

### For Students with No Programming Experience

1. **Use analogies**:
   - Variables = labeled boxes that hold values
   - Functions = recipes (inputs → process → output)
   - Lists = shopping lists with numbered items
   - For loops = repeating an action multiple times

2. **Common pain points**:
   - **Indentation**: Python is strict! Use Colab's auto-indent
   - **Parentheses**: Must match opening and closing
   - **Variable names**: Case-sensitive, no spaces
   - **Error messages**: Read from bottom up, focus on line numbers

3. **Debugging strategies**:
   - Print intermediate values
   - Check variable types
   - Run cells one at a time
   - Comment out problematic lines

4. **Encouragement**:
   - Everyone makes mistakes (even experienced programmers!)
   - Error messages are helpful, not punishments
   - Copy-paste is fine while learning
   - Focus on understanding, not memorizing

### Statistical Concepts

1. **Autocorrelation**:
   - Use the robot failure example from the case
   - Draw timeline showing consecutive delays
   - Contrast with coin flips (no correlation)

2. **Confidence intervals**:
   - Use weather forecast analogy
   - "90% confident" ≠ "exactly 90%"
   - Trade-off: higher confidence = longer due date

3. **Central Limit Theorem**:
   - Don't dive deep into theory
   - Focus on practical application
   - Emphasize "sum of many random variables → Normal"

## Assessment Rubric

### Notebook Completion (60 points)
- All TODO sections completed correctly (30 pts)
- Code runs without errors (15 pts)
- Outputs match expected values (10 pts)
- Reflection questions answered (5 pts)

### Streamlit App (30 points)
- App runs successfully (10 pts)
- Correct calculations (10 pts)
- User interface improvements (5 pts)
- Code documentation (5 pts)

### Understanding (10 points)
- Can explain autocorrelation (3 pts)
- Can explain safety time (3 pts)
- Can interpret confidence intervals (4 pts)

## Common Student Questions & Answers

**Q: Why do we use `ddof=1` in variance calculation?**
A: This gives us the "sample variance" which is more accurate for estimating population variance. The technical reason involves dividing by (n-1) instead of n.

**Q: What if autocorrelation is negative?**
A: Negative autocorrelation means high values tend to be followed by low values (alternating pattern). The formula still works, but you'd get a smaller variance multiplier.

**Q: Why not just use the maximum inter-throughput time?**
A: That would be too conservative (overly pessimistic). We want a balance between reliability and competitiveness.

**Q: Can I use this for other types of production?**
A: Absolutely! This approach works for any process with measurable throughput, as long as the throughput is stationary (no trends).

**Q: What if I can't install Streamlit?**
A: Use Streamlit Cloud (share.streamlit.io) which is free and runs in the browser. No installation needed!

## Extensions & Advanced Topics

For advanced students or extra credit:

1. **Multiple confidence levels**: Plot due dates vs. confidence levels
2. **Batch size analysis**: How does order size affect due date?
3. **Seasonality**: What if throughput varies by day/month?
4. **Real data**: Students collect their own throughput data
5. **Comparison**: Compare with vs. without autocorrelation correction

## Resources

### Python Learning
- [Python for Everybody](https://www.py4e.com/) - Free course
- [Real Python](https://realpython.com/) - Tutorials
- [Google Colab Intro](https://colab.research.google.com/notebooks/intro.ipynb)

### Streamlit
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Gallery](https://streamlit.io/gallery) - Example apps
- [Streamlit Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)

### Statistics
- [Seeing Theory](https://seeing-theory.brown.edu/) - Visual statistics
- [StatQuest YouTube](https://www.youtube.com/c/joshstarmer) - Clear explanations

## Troubleshooting

### Google Colab Issues
- **"Runtime disconnected"**: Reconnect and rerun cells
- **Cells won't run**: Check if previous cells ran successfully
- **Import errors**: Make sure first cell was executed

### Streamlit Issues
- **"Module not found"**: Install using `pip install streamlit pandas numpy scipy matplotlib`
- **Port already in use**: Stop other Streamlit apps or use `streamlit run app.py --server.port 8502`
- **CSV upload fails**: Check file format (one column, correct header)

### Statistical Issues
- **Negative variance**: Check for data entry errors
- **Very high autocorrelation**: May indicate non-stationary process
- **Unrealistic due dates**: Verify input units (hours vs. days)

## Adaptation Suggestions

### For Different Time Constraints
- **1 week condensed**: Use complete notebook, modify Streamlit app only
- **2 weeks standard**: Full template notebook + basic Streamlit
- **4 weeks extended**: Add real data collection project

### For Different Skill Levels
- **Absolute beginners**: More guided completion, pair programming
- **Some experience**: Reduce scaffolding, add challenges
- **Advanced**: Build from scratch, add features

### For Different Contexts
- **Operations management**: Emphasize business decisions
- **Data science**: Focus on statistical methods
- **Programming course**: Emphasize code structure and best practices

## Support & Feedback

For questions or suggestions about these materials:
- Check the comments in the code
- Review the reflection questions
- Consult the complete notebook for solutions

Remember: The goal is understanding, not perfection. Encourage students to experiment, make mistakes, and learn from them!
