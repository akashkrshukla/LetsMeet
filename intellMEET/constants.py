CANDIDATE_IMAGE_PLACE_HOLDER = "assets/img/avatar.jpg"

# for JobPosition status is taken is taken as 1 character.
job_position = {'CLOSED_CODE': 0, 'ACTIVE_CODE': 1, 'SUBMITTED_CODE': 4, 'FINAL_INTERVIEW_CODE': 5,
                'OFFER_ACCEPTED': 6, 'ARCHIVED_CODE': 7, 'ON_HOLD': 8}

# Reference: job_application status code taken is varchar.
# below status are applicable.
# SHORT_LISTED
# ACTIVE
# CLOSED
# ARCHIVED


interview_stage = {'CLOSED_CODE': 0, 'REQUESTED_CODE': 1, 'REGISTERED_CODE': 2, 'ACCEPTED_CODE': 3,
                   'ONE_WAY_SUBMITTED': 4, 'ONE_WAY_REVIEWED': 5, 'SHORTLISTED': 6, 'ONE_WAY_REJECTED': 7,
                   'ONHOLD': 8, 'LIVE_INTERVIEW_SCHEDULED': 9, 'LIVE_INTERVIEW_IN_PROGRESS': 10,
                   'LIVE_INTERVIEW_SUBMITTED': 11, 'LIVE_INTERVIEW_REVIEWED': 12, 'ACCEPTED': 13,
                   'LIVE_REJECTED': 14
                   }
# interview stages with !(ONHOLD, ACCEPTED, CLOSED, REQUESTED,)

UNRESPONSIVE_JOBS_DURATION_DAYS = 7
ACCOUNT_MANAGER_ROLE = 'A'  # show all data
RECRUITER_ROLE = 'R'  # show data created by user
HIRING_MANAGER_ROLE = 'H'  # show all data
INTERVIEWER_ROLE = 'I'  # carries out the interview.

# one way interview
ONE_WAY = "ONE_WAY_INTERVIEW"
LIVE_INTERVIEW = "LIVE_INTERVIEW"

LIMITED_DATA_DISPLAY_COUNT = 7
