#wx python must be used to run this code
import wx
import datetime

# This function runs when the button is clicked
def calculate_age(event):
    try:
        # Converts the text input to int input
        day = int(day_box.GetValue())
        month = int(month_box.GetValue())
        year = int(year_box.GetValue())

        # Create date of birth
        dob = datetime.date(year, month, day)

        # Get today's date
        today = datetime.date.today()

        # Find difference
        age_years = today.year - dob.year
        age_months = today.month - dob.month
        age_days = today.day - dob.day

        # If days are negative, adjust months and days
        if age_days < 0:
            age_months = age_months - 1

            # Find days in previous month
            if today.month == 1:
                prev_month = 12
                prev_year = today.year - 1
            else:
                prev_month = today.month - 1
                prev_year = today.year

            days_in_prev_month = (datetime.date(prev_year, prev_month + 1, 1) -
                                  datetime.date(prev_year, prev_month, 1)).days

            age_days = age_days + days_in_prev_month

        # If months are negative, adjust years and months
        if age_months < 0:
            age_years = age_years - 1
            age_months = age_months + 12

        # Show result in the label
        result_text.SetLabel(
            "Your age is:\n"
            + str(age_years) + " Years "
            + str(age_months) + " Months "
            + str(age_days) + " Days"
        )

    except:
        # If user enters wrong input
        wx.MessageBox(
            "Please enter valid numbers for Day, Month and Year",
            "Error",
            wx.OK | wx.ICON_ERROR
        )

app = wx.App()


frame = wx.Frame(None, title="Age Calculator", size=(350, 350))


panel = wx.Panel(frame)

# Title
title = wx.StaticText(panel, label="AGE CALCULATOR")
font = title.GetFont()
font.PointSize = 14
font = font.Bold()
title.SetFont(font)

# Day input
day_label = wx.StaticText(panel, label="Enter Birth Day (1-31):")
day_box = wx.TextCtrl(panel)

# Month input
month_label = wx.StaticText(panel, label="Enter Birth Month (1-12):")
month_box = wx.TextCtrl(panel)

# Year input
year_label = wx.StaticText(panel, label="Enter Birth Year (e.g. 2005):")
year_box = wx.TextCtrl(panel)

# Button
calc_btn = wx.Button(panel, label="Calculate Age")
calc_btn.Bind(wx.EVT_BUTTON, calculate_age)

# Result label
result_text = wx.StaticText(panel, label="Age will be shown here")

# Layout
box = wx.BoxSizer(wx.VERTICAL)
box.Add(title, 0, wx.ALL | wx.CENTER, 10)
box.Add(day_label, 0, wx.LEFT | wx.TOP, 10)
box.Add(day_box, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
box.Add(month_label, 0, wx.LEFT | wx.TOP, 10)
box.Add(month_box, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
box.Add(year_label, 0, wx.LEFT | wx.TOP, 10)
box.Add(year_box, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
box.Add(calc_btn, 0, wx.ALL | wx.CENTER, 10)
box.Add(result_text, 0, wx.ALL | wx.CENTER, 10)

panel.SetSizer(box)

# Show window
frame.Show()

# Keep app running
app.MainLoop()
