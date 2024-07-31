from django.shortcuts import render, redirect
from .models import Calendar, Reservation
from .forms import ReservationForm
import datetime
import calendar

def calendar_view(request, year=None, month=None):
    # 今日の日付を取得
    today = datetime.date.today()
    year = year or today.year
    month = month or today.month

    # 今日から30日後の日付を計算
    thirty_days_later = today + datetime.timedelta(days=30)

    # 月のカレンダーを取得
    cal = calendar.Calendar(firstweekday=6)  # 日曜日を週の始まりとする
    month_days = cal.monthdatescalendar(year, month)
    
    # 店舗の休日を取得
    store_holidays = Calendar.objects.values_list('date', flat=True)
    
    # 前月と翌月を計算
    prev_month = (month - 1) or 12
    prev_year = year if month > 1 else year - 1
    next_month = (month + 1) if month < 12 else 1
    next_year = year if month < 12 else year + 1
    
    # 現在の月が今日の月か次の月かを確認
    is_current_or_next_month =  (today.year == year and today.month == month - 1) or (today.year == prev_year and today.month == prev_month)

    # 時間スロットを準備
    time_slots = ["11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00"]
    
    # 予約フォームを作成
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar_view_month', year=year, month=month)
    else:
        form = ReservationForm()

    context = {
        'today': today,
        'year': year,
        'month': month,
        'month_days': month_days,
        'store_holidays': store_holidays,
        'prev_month': prev_month,
        'prev_year': prev_year,
        'next_month': next_month,
        'next_year': next_year,
        'is_current_or_next_month': is_current_or_next_month,
        'time_slots': time_slots,
        'form': form,
        'thirty_days_later': thirty_days_later,
    }
    return render(request, 'calendar.html', context)
