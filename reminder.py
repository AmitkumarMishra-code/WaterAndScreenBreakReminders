import time
from plyer import notification
import random
import os

dirname = os.path.dirname(__file__)

water_quotes = [
	"In general, you should try to drink between half an ounce and an ounce of water for each pound you weigh, every day.",
	"The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
	"To prevent dehydration, you need to get plenty of water from drink and food every day.",
	"The body constantly loses water throughout the day, mostly through urine and sweat but also from regular body functions like breathing.",
	"Health experts commonly recommend eight 8-ounce glasses, which equals about 2 liters, or half a gallon a day.",
	"You will need more water in hot, humid, or dry areas. You'll also need more water if you live in the mountains or at a high altitude.",
	"Even mild dehydration can reduce physical performance.",
	"Losing 1 percent of body weight might not seem like a lot, but it's a significant amount of water to lose.",
	"Mild dehydration caused by exercise or heat can have negative effects on both your physical and mental performance."
	]

lookaway_quotes = [
	"The HSE suggest that short, frequent breaks are better than less frequent longer breaks, so a 5-10 minute break after 50-60 minutes is better than a 20 minute break every 3 hours",
	"Taking a break from the screen will help you bring balance to your digital and real-world lives",
	"Computer vision syndrome (CVS) is strain on the eyes that happens when you use a computer or digital device for prolonged periods of time.",
	"Eye strain from hours of screen time can result in eye irritation, dryness, fatigue or blurred vision, and such problems are increasingly common, according to a new report.",
	"Stepping away from technology not only gives your brain a break but also gives you the added bonus of perspective.",
	"By taking a mini digital detox from tech on a daily basis, you will not only feel recharged every day, but you'll see a boost in your productivity levels at work!"
]

count = 1

while True:
	notification.notify(
		title="Water Break!!",
		message=random.choice(water_quotes),
		app_icon=os.path.join(dirname, "icon.ico"),
		timeout=12
	)

	if count % 2 == 0:
		time.sleep(10)
		notification.notify(
			title="Screen Break!!",
			message=random.choice(lookaway_quotes),
			app_icon=os.path.join(dirname, "screen.ico"),
			timeout=12
		)
	if count == 10:
		count = 0
	count += 1
	time.sleep(15 * 60)



