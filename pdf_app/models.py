# from django import forms
#
#
# class Order(forms.Form):
#     id = forms.CharField(max_length=255 )  # "17696",
#     createDate = forms.CharField(max_length=255 )  # "24.05.2019",
#     expressID = forms.CharField(max_length=255 )  # "73792751430636",
#     createTime = forms.CharField(max_length=255 )  # "14:53"
#
# class DateTime(forms.Form):
#     days = forms.IntegerField()  # 0,
#     hours = forms.IntegerField()  # 9,
#     minutes = forms.IntegerField()  # 46,
#     seconds = forms.IntegerField()  # 0
#
#
# class CarType(forms.Form):
#     type = forms.CharField(max_length=255 )  # 3У or ОКТ
#
#
# class Carrier(forms.Form):
#     content = forms.CharField(max_length=255 )  # "ОАО \"РЖД\"",
#     name = forms.CharField(max_length=255 )  # null,
#     country = forms.CharField(max_length=255 )  # "20",
#     inn = forms.CharField(max_length=255 )  # "7708503727",
#     code = forms.CharField(max_length=255 )  # null
#
#
# class CarTrain(forms.Form):
#     # id = forms.CharField(max_length=255)
#     type = forms.CharField(max_length=255 )  # "ПЛАЦ",
#     number = forms.CharField(max_length=255 )  # "05",
#     owner = forms.ForeignKey(CarType)
#     tripClass = forms.CharField(max_length=255 )  # null,
#     carrier = forms.ForeignKey(Carrier)
#     classService = forms.ForeignKey(CarType)
#     addSigns = forms.CharField(max_length=255 )  # "У0"
#
#
#
# class DepartArrive(forms.Form):
#     time = forms.CharField(max_length=255 )  # "01:25",
#     date = forms.CharField(max_length=255 )  # "31.05.2019",
#     stationCode = forms.CharField(max_length=255 )  # "2006004",
#     trainType = forms.CharField(max_length=255 )  # "СКОРЫЙ",
#     trainCat = forms.CharField(max_length=255 )  # null,
#     station = forms.CharField(max_length=255 )  # "МОСКВА ОКТЯБРЬСКАЯ (ЛЕНИНГРАДСКИЙ ВОКЗАЛ)",
#     train = forms.CharField(max_length=255 )  # "128АА",
#     localTime = forms.CharField(max_length=255 )  # null,
#     localDate = forms.CharField(max_length=255 )  # null
#
#
# class Seat(forms.Form):
#     content = forms.CharField(max_length=255 )  # "016",
#     count = forms.CharField(max_length=255 )  # "01"
#
#
# class Wiparam(forms.Form):
#     db = forms.CharField(max_length=255 )  # "Ф",
#     hp = forms.CharField(max_length=255 )  # "001",
#     ht = forms.CharField(max_length=255 )  # "02",
#     wm = forms.CharField(max_length=255 )  # null,
#     wb = forms.CharField(max_length=255 )  # "М"
#
#
# class Train(forms.Form):
#     date = forms.CharField(max_length=255 )  # 31.05.2019"
#
#
# class Passenger(forms.Form):
#     name = forms.CharField(max_length=255 )  # "ЖОЛДЫБАЕВ=НУРЛАН=БАХТЫБАЕВИЧ",
#     doc = forms.CharField(max_length=255 )  # "ПН9701323455",
#     sex = forms.CharField(max_length=255 )  # "F",
#     citizenship = forms.CharField(max_length=255 )  # "RUS",
#     birthday = forms.CharField(max_length=255 )  # "29.04.1998"
#
#
# class TicketChild(forms.Form):
#     electronicTicketReg = forms.BooleanField()  # false,
#     refoundTicket = forms.BooleanField()  # false,
#     number = forms.CharField(max_length=10)  # "1",
#     id = forms.CharField(max_length=255 )  # "22795",
#     tariff = forms.CharField(max_length=255 )  # "455361",
#     passenger = forms.ForeignKey(Passenger)
#     expressID = forms.CharField(max_length=255 )  # "73792751430636",
#     elRegPossible = forms.CharField(max_length=255 )  # "notFound",
#     seats = forms.CharField(max_length=255 )  # "016",
#     tariffEuro = forms.CharField(max_length=255 )  # null,
#     numberReservation = forms.CharField(max_length=255 )  # null,
#     tariffVedServiceNDS = forms.CharField(max_length=255 )  # null,
#     listPassIssued = forms.CharField(max_length=255 )  # null,
#     tariffVedService = forms.CharField(max_length=255 )  # null,
#     tariffServiceNDS = forms.CharField(max_length=255 )  # "0",
#     tariffVedComNDS = forms.CharField(max_length=255 )  # null,
#     tariffLoyalLost = forms.CharField(max_length=255 )  # null,
#     tariffInsurance = forms.CharField(max_length=255 )  # "0",
#     tariffComNDS = forms.CharField(max_length=255 )  # "0",
#     tariffCom = forms.CharField(max_length=255 )  # "95000",
#     tariffBP = forms.CharField(max_length=255 )  # "360361",
#     ndsRate1 = forms.CharField(max_length=255 )  # "00.0",
#     tariffService = forms.CharField(max_length=255 )  # "18446",
#     ndsRate3 = forms.CharField(max_length=255 )  # "00.0",
#     tariffP = forms.CharField(max_length=255 )  # "99209",
#     tariffNDS = forms.CharField(max_length=255 )  # "0",
#     ndsRate2 = forms.CharField(max_length=255 )  # "00.0",
#     tariffB = forms.CharField(max_length=255 )  # "261152",
#     tariffType = forms.CharField(max_length=255 )  # "ПОЛНЫЙ",
#     vedTT = forms.CharField(max_length=255 )  # null,
#     passCount = forms.CharField(max_length=255 )  # "01",
#     tariffInfo = forms.CharField(max_length=255 )  # null,
#     tariffVedCom = forms.CharField(max_length=255 )  # null,
#     d5 = forms.CharField(max_length=255 )  # "",
#     tariffVed = forms.CharField(max_length=255 )  # null,
#     tariffVedNDS = forms.CharField(max_length=255 )  # null,
#     privilegeTT = forms.CharField(max_length=255 )  # null,
#     seatsType = forms.CharField(max_length=255 )  # "В",
#     tariffCredit = forms.CharField(max_length=255 )  # null
#
#
# class TicketParent(forms.Form):
#     ticket = forms.ForeignKey(TicketChild)
#
#
# class ResponseBuyTicket(forms.Form):
#     hasError = forms.BooleanField()
#     directionType = forms.CharField(max_length=255),
#     type = forms.CharField(max_length=255),
#     order = forms.ForeignKey(Order),
#     tickets = forms.ForeignKey(TicketParent),
#     car = forms.ForeignKey(CarTrain),
#     tariff = forms.CharField(max_length=255),  # "455361",
#     departure = forms.ForeignKey(DepartArrive),
#     arrival = forms.ForeignKey(DepartArrive),
#     seats = forms.ForeignKey(Seat),
#     paymentType = forms.CharField(max_length=255),  # "Н",
#     agent = forms.CharField(max_length=255),  # "УТИ",
#     subagent = forms.CharField(max_length=255 ),  # null,
#     wiparam = forms.ForeignKey(Wiparam),
#     saleOnTwo = forms.CharField(max_length=255 ),  # null,
#     signGA = forms.CharField(max_length=255),  # "ПОЛУЧИТЬ БИЛЕТ НА СТАНЦИИ ОТПРАВЛЕНИЯ НЕЛЬЗЯ",
#     tariffEuro = forms.CharField(max_length=255 ),  # null,
#     signR = forms.CharField(max_length=255 ),  # null,
#     carrier = forms.ForeignKey(Carrier),
#     signGB = forms.CharField(max_length=255),  # "ВРЕМЯ ОТПРАВЛЕНИЯ МОСКОВСКОЕ",
#     departureTrain = forms.ForeignKey(Train),
#     errorResp = forms.CharField(max_length=255),  # null
#
#
# class TicketPurchase(forms.Form):
#     identifier = forms.CharField(max_length=255 )  # 316a0193-3eee-40f0-8ec2-9ceb066ec1cd",
#     exspOrderID = forms.CharField(max_length=255 )  # 17696",
#     passangers = forms.IntegerField()  # 2,
#     adultPass = forms.IntegerField()  # 1,
#     withoutRevengePass = forms.IntegerField()  # 1,
#     directionType = forms.CharField(max_length=255 )  # Forward",
#     createTime = forms.TextField()
#     trainDepartureDateTime = forms.TextField()
#     trainArrivalDateTime = forms.TextField()
#     timeInWay = forms.ForeignKey(DateTime)
#     totalCost = forms.IntegerField()  # 455361.00,
#     responseBuyTicket = forms.ForeignKey(ResponseBuyTicket)
#     orderID = forms.CharField(max_length=255 )  # ed4bc189-f072-48be-bda4-a882eab066c0",
#     userId = forms.CharField(max_length=255 )  # a9bcd0bc-5656-4450-80eb-8a4e70c9c6c3"
