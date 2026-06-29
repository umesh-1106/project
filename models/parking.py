# ============================================
# Wrong Parking Detection Logic
# ============================================

# Restricted Areas
RESTRICTED_AREAS = [
    "College Main Gate",
    "Emergency Exit",
    "Fire Exit",
    "No Parking Zone",
    "Staff Entrance"
]


class ParkingChecker:

    def __init__(self):
        self.restricted_areas = RESTRICTED_AREAS

    def is_wrong_parking(self, location):

        if location in self.restricted_areas:
            return True

        return False


parking_checker = ParkingChecker()
