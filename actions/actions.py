# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# class ActionAskName(Action):
#     def name(self) -> str:
#         return "utter_ask_name"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
#         dispatcher.utter_message(text="Xin vui lòng cung cấp tên của bạn để tôi có thể xác nhận đặt bàn.")
#         return []

# class ActionAskPhone(Action):
#     def name(self) -> str:
#         return "utter_ask_phone"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
#         dispatcher.utter_message(text="Xin vui lòng cung cấp số điện thoại của bạn.")
#         return []

# class ActionConfirmBooking(Action):
#     def name(self) -> str:
#         return "action_confirm_booking"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
#         name = next(tracker.get_latest_entity_values("name"), "Khách hàng")
#         phone = next(tracker.get_latest_entity_values("phone"), "Không có số điện thoại")
#         number_of_people = next(tracker.get_latest_entity_values("number_of_people"), "không xác định")
#         time = next(tracker.get_latest_entity_values("time"), "không xác định")
#         table_type = next(tracker.get_latest_entity_values("table_type"), "không xác định")

#         dispatcher.utter_message(
#             text=f"Đặt bàn thành công cho {name} ({phone}) với {number_of_people} người vào lúc {time}, loại bàn: {table_type}. Cảm ơn bạn!"
#         )
#         return []

# class ActionShowPromotions(Action):
#     def name(self) -> str:
#         return "action_show_promotions"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
#         promotions = ["Giảm giá 10% cho tất cả các món ăn", "Combo 2 món với giá ưu đãi", "Miễn phí trà đá cho mỗi bàn ăn"]
#         dispatcher.utter_message(text="Hiện tại chúng tôi có các chương trình khuyến mãi sau:\n" + "\n".join(promotions))
#         return []

# class ActionCancelBooking(Action):
#     def name(self) -> str:
#         return "action_cancel_booking"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
#         dispatcher.utter_message(text="Đặt bàn của bạn đã được hủy thành công. Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi.")
#         return []
