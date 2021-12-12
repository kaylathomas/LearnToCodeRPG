# creators should use priorities in the range -999 to 999
# run last
init 998:
    default stats_unlocked = False
    default stats_knowledge_unlocked = False # cs knowledge
    default stats_subcategory_unlocked = False # subcategory of cs knowledge
    default todo_unlocked = False

    # alternative endings
    default has_triggered_ending_barista = False
    default has_triggered_ending_cat = False
    default has_triggered_ending_tutor = False
    default has_triggered_ending_office = False

    default num_times_sanity_low = 0
    default has_triggered_ending_farmer = False

    default has_triggered_ending_today = False

    # set question type during study session
    # default study_session_questions = general_questions
    default study_session_questions = css_questions

    default has_visited_hacker_space_with_annika = False

    # unlocks Marco's topics_to_ask
    default has_met_marco = False

    # major characters and plot have been introduced, unlocks alternative endings
    default has_met_layla = False

    # once this is True, trivia guy no longer appears, and player can get a first round interview w/ CupCakeCPU
    default has_won_hacker_space_trivia = False
    default has_applied_to_cupcakecpu = False

    define cs_knowledge_threshold = 60 # need 60 CS Knowledge to pass the curriculum
    # player_stats.player_stats_map['CS Knowledge'] >= cs_knowledge_threshold
    default has_completed_curriculum = False

    default num_jobs_applied = 0
    default num_jobs_interviewed = 0
    default num_jobs_rejected = 0
    default num_offers = 0 # v2

    default has_received_offer = False
    # TODO: beyond demo version, can do negotiation
    default has_accepted_offer = False # v2

    default day_activity = None # set in day_activity_choice.rpy

    # interview and offer
    default interview_company_name = None # set in day_activity_choice.rpy
    default offer_company_name = None # set in quiz_session.rpy

    # seen labels
    default seen_hacker_space_events = set()
    default seen_barista_events = set()

    default persistent.enable_save_reminder = None

init python:
    if persistent.achievements is None:
        persistent.achievements = set()

    # npc Q and A
    topics_to_ask = set()
    npc = annika
    npc_sprite = 'annika'

    ## Non-mutable

    ## Note to proofreader: please proofread these; they show up as To-Do items
    # to-do strings
    todo_check_fcc = 'Check out [freeCodeCamp]'
    todo_ask_curriculum = 'Ask Annika about CS curriculum'
    todo_learn_cs = 'Bump {b}CS Knowledge{/b} to [cs_knowledge_threshold]+'
    todo_apply_cupcakecpu = 'Apply to CupcakeCPU'
    todo_apply_to_jobs = 'Start applying to jobs'
    todo_interview_prep = 'Start preparing for coding interviews'
    todo_get_job = 'Get a developer job'
    todo_ask_hackathon = 'Learn about Hackathon'
    todo_ask = 'Learn about ' # should be concatenated with vocabs from barista story

    ## Note to proofreader: please do not change these labels
    # story labels for hacker space and barista
    hacker_space_event_labels = [
    'hacker_space_tech_talk',
    'hacker_space_playtest',
    'hacker_space_project',
    'hacker_space_open_source',
    ]

    barista_event_labels = [
    'barista_fullstack',
    'barista_devops',
    'barista_conference',
    'barista_versioncontrol',
    'barista_machinelearning',
    'barista_agile',
    'barista_api',
    'barista_userexperience',    
    ]

    # map topic to label name
    ask_npc = {
    'Hackathon': 'ask_hackathon',
    'Full-Stack': 'ask_fullstack',
    'DevOps': 'ask_devops',
    'Conference': 'ask_conference',
    'Version Control': 'ask_versioncontrol',
    'Machine Learning': 'ask_machinelearning',
    'Agile': 'ask_agile',
    'API': 'ask_api',
    'User Experience': 'ask_userexperience',
    }

    # VIP names and profile links
    # TODO: add other contributors
    vip_names = {
    'Quincy': 'https://twitter.com/ossia', 
    'Lynn': 'https://ruolinzheng08.github.io/',
    'Abbey': 'https://twitter.com/abbeyrenn', 
    }

    # Note to proofreader: please proofread the tweet content
    tweet_default = generate_tweet_intent('I just discovered this cool game called #LearnToCodeRPG. Play it here: ')

    # Note to proofreader: these are achievement strings displayed on the Achievements screen. Please proofread
    # Please check the casing of the title
    ## milestone
    milestone_complete_curriculum = 'Nailed the Curriculum!'
    milestone_first_interview = 'Got My First Interview!'
    milestone_first_offer = 'Got My First Offer!'
    # TODO: v2 can have multiple offers
    milestone_sign_offer = 'Now Streaming: My Dream Dev Job'

    tweet_complete_curriculum = tweet_default
    tweet_first_interview = tweet_default
    tweet_first_offer = tweet_default
    tweet_sign_offer = tweet_default

    milestone_to_tweet_map = {
        milestone_complete_curriculum: tweet_complete_curriculum,
        milestone_first_interview: tweet_first_interview,
        milestone_first_offer: tweet_first_offer,
        milestone_sign_offer: tweet_sign_offer
    }

    ## plot easter eggs
    plot_cookie = 'Late-night Cookie Crunch'
    plot_trivia = 'Tech Trivia Guru'
    plot_quiz_all = 'Nailed All Quizzes in a Session'
    plot_quiz_none = 'Bombed All Quizzes in a Session'
    plot_hackerspace = 'Hanging out at the Hacker Space'

    # TODO: vip, barista, hackerspace, minigame, saving up all buzzwords, asking all to Marco or all to Annika
    # too chill etc.
    plot_skill_coffee = 'This Job Needs Me to Brew Coffee?'
    plot_skill_fax = 'This Job Needs Me to Fix Fax Machiens?'
    plot_skill_customer = 'This Job Needs Me to Handle Angry Customers?'
    plot_skill_cable = 'This Job Needs Me to Fuse Cables?'
    plot_skill_password = 'This Job Needs Me to Retrieve Lost Passwords?'
    plot_skill_pet = 'This Job Needs Me to Pacify Office Pets?'

    plot_double_check = 'You Can Never Be Too Careful with Prod'

    tweet_hackerspace = generate_tweet_intent('I just discovered the Hackerspace in #LearnToCodeRPG. Play it here: ')
    tweet_weird_job_skill = tweet_default

    # TODO: none default tweet
    plot_bonus_to_tweet_map = {
        plot_cookie: tweet_default,
        plot_trivia: tweet_default,
        plot_quiz_all: tweet_default,
        plot_quiz_none: tweet_default,
    }

    ## quiz
    # questions that have a `wait thats not a cs question` label
    # quiz_fcc_history

    quiz_fcc_launch = "The Launch of freeCodeCamp"
    quiz_fcc_mission = "The Mission of freeCodeCamp"
    quiz_code_radio = "Hello, Earth to Code Radio!"
    quiz_devdocs = "Dr. DevDocs.io"
    quiz_fcc_opensource = 'Contribute to Open Source with freeCodeCamp!'
    quiz_fcc_language = 'The Tech Stack of freeCodeCamp'
    quiz_fcc_inspiration = 'What inspired freeCodeCamp?'
    quiz_fcc_forum = 'freeCodeCamp Has a Forum? Neat!'
    quiz_fcc_chat = 'freeCodeCamp Has a Chat Server? Fancy!'
    quiz_fcc_mascot = 'freeCodeCamp Has a Mascot? Cute!'

    quiz_bonus_to_tweet_map = {
        quiz_fcc_launch: tweet_default,
        quiz_fcc_mission: tweet_default,
        quiz_code_radio: tweet_default,
        quiz_devdocs: tweet_default,
        quiz_fcc_opensource: tweet_default,
        quiz_fcc_language: tweet_default,
        quiz_fcc_inspiration: tweet_default,
        quiz_fcc_forum: tweet_default,
        quiz_fcc_chat: tweet_default,
        quiz_fcc_mascot: tweet_default
    }

    ## endings
    ending_barista = 'Now serving {font=fonts/saxmono.ttf}0xc0ffee{/font}'
    ending_cat = 'Cat Who Codes'
    ending_tutor = 'Coding It Forward'
    ending_office = 'Just Another Day at the Office'
    ending_farmer = 'Nature Lover at Heart'
    ending_dev = 'Dev Who Brought Down Prod on the First Day'

    tweet_end_barista = 'https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.freecodecamp.org%2Flearn-to-code-rpg&text=I%20ended%20up%20becoming%20a%20barista%20in%20%23LearnToCodeRPG.%20Play%20it%20here%3A'
    tweet_end_cat = 'https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.freecodecamp.org%2Flearn-to-code-rpg&text=I%20found%20my%20cat%20coding%20on%20my%20laptop%20in%20the%20middle%20of%20the%20night%20in%20%23LearnToCodeRPG.%20Play%20it%20here%3A'
    tweet_end_tutor = 'https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.freecodecamp.org%2Flearn-to-code-rpg&text=I%20ended%20up%20becoming%20a%20CS%20teacher%20in%20%23LearnToCodeRPG.%20Play%20it%20here%3A'
    tweet_end_office = 'https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.freecodecamp.org%2Flearn-to-code-rpg&text=I%20ended%20up%20becoming%20an%20office%20worker%20in%20%23LearnToCodeRPG.%20Play%20it%20here%3A'
    tweet_end_farmer = 'https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.freecodecamp.org%2Flearn-to-code-rpg&text=I%20ended%20up%20becoming%20a%20farmer%20in%20%23LearnToCodeRPG.%20Play%20it%20here%3A'
    tweet_end_dev = 'https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.freecodecamp.org%2Flearn-to-code-rpg&text=I%20taught%20myself%20to%20code%2C%20got%20a%20tech%20job%2C%20and%20brought%20down%20prod%20on%20my%20first%20day%20of%20work%20in%20%23LearnToCodeRPG.%20Play%20it%20here%3A'

    ending_to_tweet_map = {
        ending_barista: tweet_end_barista,
        ending_cat: tweet_end_cat,
        ending_tutor: tweet_end_tutor,
        ending_office: tweet_end_barista,
        ending_farmer: tweet_end_farmer,
        ending_dev: tweet_end_dev,
    }

    ## master labels and maps
    plot_achievement = 'Story Milestones'
    plot_bonus = 'Story Easter Eggs'
    quiz_bonus = 'Quiz Question Easter Eggs'
    ending_achievement = 'Endings'

    achievement_labels_map = {
        plot_achievement: milestone_to_tweet_map,
        plot_bonus: plot_bonus_to_tweet_map,
        quiz_bonus: quiz_bonus_to_tweet_map,
        ending_achievement: ending_to_tweet_map
    }

    # master map for easy lookup in script.rpy
    all_tweet_map = {}
    for tweet_map in achievement_labels_map.values():
        all_tweet_map.update(tweet_map)

    total_num_achievements = len(all_tweet_map)
    # all achievements unlocked
    tweet_all_achievements_unlocked = tweet_default    

    # skills
    all_questions_map = {
    'CSS': css_questions,
    'HTML': html_questions,
    'Git': git_questions,
    'IT': it_questions,
    'JavaScript': javascript_questions,
    'Linux': linux_questions,
    'Python': python_questions,
    'SQL': sql_questions
    }

    # assign category to questions
    for category in all_questions_map:
        for question in all_questions_map[category]:
            question.category = category

    # master list of questions for mix-and-match
    all_quiz_questions = []
    for question_list in all_questions_map.values():
        all_quiz_questions.extend(question_list)

    # the order is important
    all_skills = [
    'HTML',
    'CSS',
    'JavaScript',
    'Python',
    'Linux',
    'Git',
    'SQL',
    'IT',
    ]
