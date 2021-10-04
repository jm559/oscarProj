from searchMovie import searchByCategory, searchByYear, searchByWinner, searchByName, data
import json
import unittest

class MyTest(unittest.TestCase):
    
    def test_name(self):
        x1 = [{'year': 1953, 'category': ['ART DIRECTION (Black-and-White)', 'WRITING (Story and Screenplay)', 'ACTRESS IN A LEADING ROLE', 'ACTRESS IN A SUPPORTING ROLE', 'ART DIRECTION', 'CINEMATOGRAPHY', 'COSTUME DESIGN', 'DIRECTING', 'FILM EDITING', 'MAKEUP', 'MUSIC (Original Dramatic Score)', 'MUSIC (Original Song)', 'BEST PICTURE', 'SOUND', 'SOUND EFFECTS EDITING', 'VISUAL EFFECTS'], 'name': 'Art Direction:  Lyle Wheeler, Maurice Ransford;  Set Decoration:  Stuart Reiss', 'film': 'Titanic', 'winner': False}] 
        x = searchByName("Titanic", data)
        
        #tested against expect answer, is not none, and no result
        self.assertEqual(x, x1)
        self.assertIsNot(x, [])
        self.assertEqual(searchByName("Scooby doo", data), [])
       
    def test_category(self):
        x = searchByCategory("Best Motion Picture", data)
        x1 = [{'year': 1944, 'category': ['BEST MOTION PICTURE', 'SOUND RECORDING', 'WRITING (Screenplay)'], 'name': 'Paramount', 'film': 'Double Indemnity', 'winner': False}, {'year': 1944, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay)'], 'name': 'Metro-Goldwyn-Mayer', 'film': 'Gaslight', 'winner': False}, {'year': 1944, 'category': ['BEST MOTION PICTURE', 'WRITING (Original Motion Picture Story)', 'WRITING (Screenplay)'], 'name': 'Paramount', 'film': 'Going My Way', 'winner': True}, {'year': 1944, 'category': ['BEST MOTION PICTURE', 'SPECIAL EFFECTS'], 'name': 'Selznick International Pictures', 'film': 'Since You Went Away', 'winner': False}, {'year': 1944, 'category': ['BEST MOTION PICTURE', 'SOUND RECORDING', 'SPECIAL EFFECTS', 'WRITING (Original Screenplay)'], 'name': '20th Century-Fox', 'film': 'Wilson', 'winner': False}, {'year': 1945, 'category': ['BEST MOTION PICTURE'], 'name': 'Metro-Goldwyn-Mayer', 'film': 'Anchors Aweigh', 'winner': False}, {'year': 1945, 'category': ['BEST MOTION PICTURE', 'SOUND RECORDING'], 'name': 'Rainbow Productions', 'film': "The Bells of St. Mary's", 'winner': False}, {'year': 1945, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay)'], 'name': 'Paramount', 'film': 'The Lost Weekend', 'winner': True}, {'year': 1945, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay)'], 'name': 'Warner Bros.', 'film': 'Mildred Pierce', 'winner': False}, {'year': 1945, 'category': ['BEST MOTION PICTURE', 'SPECIAL EFFECTS', 'DOCUMENTARY (Feature)'], 'name': 'Selznick International Pictures', 'film': 'Spellbound', 'winner': False}, {'year': 1946, 'category': ['BEST MOTION PICTURE', 'SOUND RECORDING', 'WRITING (Screenplay)'], 'name': 'Samuel Goldwyn Productions', 'film': 'The Best Years of Our Lives', 'winner': True}, {'year': 1946, 'category': ['BEST MOTION PICTURE', 'ACTOR IN A LEADING ROLE', 'COSTUME DESIGN', 'DIRECTING'], 'name': 'J. Arthur Rank-Two Cities Films', 'film': 'Henry V', 'winner': False}, {'year': 1946, 'category': ['BEST MOTION PICTURE', 'SOUND RECORDING'], 'name': 'Liberty Films', 'film': "It's a Wonderful Life", 'winner': False}, {'year': 1946, 'category': ['BEST MOTION PICTURE'], 'name': '20th Century-Fox', 'film': "The Razor's Edge", 'winner': False}, {'year': 1946, 'category': ['BEST MOTION PICTURE'], 'name': 'Metro-Goldwyn-Mayer', 'film': 'The Yearling', 'winner': False}, {'year': 1947, 'category': ['BEST MOTION PICTURE', 'SOUND RECORDING'], 'name': 'Samuel Goldwyn Productions', 'film': "The Bishop's Wife", 'winner': False}, {'year': 1947, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay)'], 'name': 'RKO Radio', 'film': 'Crossfire', 'winner': False}, {'year': 1947, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay)'], 'name': '20th Century-Fox', 'film': "Gentleman's Agreement", 'winner': True}, {'year': 1947, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay)'], 'name': 'J. Arthur Rank-Cineguild', 'film': 'Great Expectations', 'winner': False}, {'year': 1947, 'category': ['BEST MOTION PICTURE', 'WRITING (Motion Picture Story)', 'WRITING (Screenplay)'], 'name': '20th Century-Fox', 'film': 'Miracle on 34th Street', 'winner': False}, {'year': 1948, 'category': ['BEST MOTION PICTURE', 'ART DIRECTION', 'COSTUME DESIGN', 'ART DIRECTION', 'COSTUME DESIGN', 'MUSIC (Original Dramatic Score)', 'WRITING (Screenplay Based on Material Previously Produced or Published)'], 'name': 'J. Arthur Rank-Two Cities Films', 'film': 'Hamlet', 'winner': True}, {'year': 1948, 'category': ['BEST MOTION PICTURE', 'SOUND RECORDING', 'WRITING (Screenplay)'], 'name': 'Warner Bros.', 'film': 'Johnny Belinda', 'winner': False}, {'year': 1948, 'category': ['BEST MOTION PICTURE', 'WRITING (Motion Picture Story)'], 'name': 'J. Arthur Rank-Archers', 'film': 'The Red Shoes', 'winner': False}, {'year': 1948, 'category': ['BEST MOTION PICTURE', 'SOUND RECORDING', 'WRITING (Screenplay)'], 'name': '20th Century-Fox', 'film': 'The Snake Pit', 'winner': False}, {'year': 1948, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay)'], 'name': 'Warner Bros.', 'film': 'The Treasure of the Sierra Madre', 'winner': False}, {'year': 1949, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay)'], 'name': 'Robert Rossen Productions', 'film': "All the King's Men", 'winner': True}, {'year': 1949, 'category': ['BEST MOTION PICTURE', 'WRITING (Story and Screenplay)'], 'name': 'Metro-Goldwyn-Mayer', 'film': 'Battleground', 'winner': False}, {'year': 1949, 'category': ['BEST MOTION PICTURE'], 'name': 'Paramount', 'film': 'The Heiress', 'winner': False}, {'year': 1949, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay)'], 'name': '20th Century-Fox', 'film': 'A Letter to Three Wives', 'winner': False}, {'year': 1949, 'category': ['BEST MOTION PICTURE', 'SOUND RECORDING'], 'name': '20th Century-Fox', 'film': "Twelve O'Clock High", 'winner': False}, {'year': 1950, 'category': ['BEST MOTION PICTURE', 'SOUND RECORDING', 'WRITING (Screenplay)'], 'name': '20th Century-Fox', 'film': 'All about Eve', 'winner': True}, {'year': 1950, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay)'], 'name': 'Columbia', 'film': 'Born Yesterday', 'winner': False}, {'year': 1950, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay)'], 'name': 'Metro-Goldwyn-Mayer', 'film': 'Father of the Bride', 'winner': False}, {'year': 1950, 'category': ['BEST MOTION PICTURE'], 'name': 'Metro-Goldwyn-Mayer', 'film': "King Solomon's Mines", 'winner': False}, {'year': 1950, 'category': ['BEST MOTION PICTURE', 'WRITING (Story and Screenplay)'], 'name': 'Paramount', 'film': 'Sunset Blvd.', 'winner': False}, {'year': 1951, 'category': ['BEST MOTION PICTURE', 'WRITING (Story and Screenplay)'], 'name': 'Arthur Freed, Producer', 'film': 'An American in Paris', 'winner': True}, {'year': 1951, 'category': ['BEST MOTION PICTURE'], 'name': 'Anatole Litvak and Frank McCarthy, Producers', 'film': 'Decision before Dawn', 'winner': False}, {'year': 1951, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay)', 'SHORT SUBJECT (Cartoon)'], 'name': 'George Stevens, Producer', 'film': 'A Place in the Sun', 'winner': False}, {'year': 1951, 'category': ['BEST MOTION PICTURE'], 'name': 'Sam Zimbalist, Producer', 'film': 'Quo Vadis', 'winner': False}, {'year': 1951, 'category': ['BEST MOTION PICTURE', 'SOUND RECORDING', 'WRITING (Screenplay)'], 'name': 'Charles K. Feldman, Producer', 'film': 'A Streetcar Named Desire', 'winner': False}, {'year': 1952, 'category': ['BEST MOTION PICTURE', 'WRITING (Motion Picture Story)'], 'name': 'Cecil B. DeMille, Producer', 'film': 'The Greatest Show on Earth', 'winner': True}, {'year': 1952, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay)'], 'name': 'Stanley Kramer, Producer', 'film': 'High Noon', 'winner': False}, {'year': 1952, 'category': ['BEST MOTION PICTURE'], 'name': 'Pandro S. Berman, Producer', 'film': 'Ivanhoe', 'winner': False}, {'year': 1952, 'category': ['BEST MOTION PICTURE', 'ACTRESS IN A LEADING ROLE', 'ART DIRECTION', 'CINEMATOGRAPHY', 'COSTUME DESIGN', 'FILM EDITING', 'MAKEUP', 'BEST PICTURE', 'SOUND'], 'name': 'Romulus Films', 'film': 'Moulin Rouge', 'winner': False}, {'year': 1952, 'category': ['BEST MOTION PICTURE', 'SOUND RECORDING', 'WRITING (Screenplay)'], 'name': 'John Ford and Merian C. Cooper, Producers', 'film': 'The Quiet Man', 'winner': False}, {'year': 1953, 'category': ['BEST MOTION PICTURE', 'SOUND RECORDING', 'WRITING (Screenplay)'], 'name': 'Buddy Adler, Producer', 'film': 'From Here to Eternity', 'winner': True}, {'year': 1953, 'category': ['BEST MOTION PICTURE'], 'name': 'John Houseman, Producer', 'film': 'Julius Caesar', 'winner': False}, {'year': 1953, 'category': ['BEST MOTION PICTURE'], 'name': 'Frank Ross, Producer', 'film': 'The Robe', 'winner': False}, {'year': 1953, 'category': ['BEST MOTION PICTURE', 'WRITING (Motion Picture Story)', 'WRITING (Screenplay)'], 'name': 'William Wyler, Producer', 'film': 'Roman Holiday', 'winner': False}, {'year': 1953, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay)'], 'name': 'George Stevens, Producer', 'film': 'Shane', 'winner': False}, {'year': 1954, 'category': ['BEST MOTION PICTURE', 'SOUND RECORDING', 'WRITING (Screenplay)'], 'name': 'Stanley Kramer, Producer', 'film': 'The Caine Mutiny', 'winner': False}, {'year': 1954, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay)'], 'name': 'William Perlberg, Producer', 'film': 'The Country Girl', 'winner': False}, {'year': 1954, 'category': ['BEST MOTION PICTURE', 'WRITING (Story and Screenplay)'], 'name': 'Sam Spiegel, Producer', 'film': 'On the Waterfront', 'winner': True}, {'year': 1954, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay)'], 'name': 'Jack Cummings, Producer', 'film': 'Seven Brides for Seven Brothers', 'winner': False}, {'year': 1954, 'category': ['BEST MOTION PICTURE'], 'name': 'Sol C. Siegel, Producer', 'film': 'Three Coins in the Fountain', 'winner': False}, {'year': 1955, 'category': ['BEST MOTION PICTURE', 'SOUND RECORDING'], 'name': 'Buddy Adler, Producer', 'film': 'Love Is a Many-Splendored Thing', 'winner': False}, {'year': 1955, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay)'], 'name': 'Harold Hecht, Producer', 'film': 'Marty', 'winner': True}, {'year': 1955, 'category': ['BEST MOTION PICTURE', 'SOUND RECORDING'], 'name': 'Leland Hayward, Producer', 'film': 'Mister Roberts', 'winner': False}, {'year': 1955, 'category': ['BEST MOTION PICTURE'], 'name': 'Fred Kohlmar, Producer', 'film': 'Picnic', 'winner': False}, {'year': 1955, 'category': ['BEST MOTION PICTURE'], 'name': 'Hal B. Wallis, Producer', 'film': 'The Rose Tattoo', 'winner': False}, {'year': 1956, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay--Adapted)'], 'name': 'Michael Todd, Producer', 'film': 'Around the World in 80 Days', 'winner': True}, {'year': 1956, 'category': ['BEST MOTION PICTURE', 'SOUND RECORDING', 'WRITING (Screenplay--Adapted)'], 'name': 'William Wyler, Producer', 'film': 'Friendly Persuasion', 'winner': False}, {'year': 1956, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay--Adapted)'], 'name': 'George Stevens and Henry Ginsberg, Producers', 'film': 'Giant', 'winner': False}, {'year': 1956, 'category': ['BEST MOTION PICTURE', 'SOUND RECORDING'], 'name': 'Charles Brackett, Producer', 'film': 'The King and I', 'winner': False}, {'year': 1956, 'category': ['BEST MOTION PICTURE', 'SOUND RECORDING', 'SPECIAL EFFECTS'], 'name': 'Cecil B. DeMille, Producer', 'film': 'The Ten Commandments', 'winner': False}, {'year': 1957, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay--based on material from another medium)'], 'name': 'Sam Spiegel, Producer', 'film': 'The Bridge on the River Kwai', 'winner': True}, {'year': 1957, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay--based on material from another medium)'], 'name': 'Jerry Wald, Producer', 'film': 'Peyton Place', 'winner': False}, {'year': 1957, 'category': ['BEST MOTION PICTURE', 'SOUND RECORDING', 'WRITING (Screenplay--based on material from another medium)'], 'name': 'William Goetz, Producer', 'film': 'Sayonara', 'winner': False}, {'year': 1957, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay--based on material from another medium)'], 'name': 'Henry Fonda and Reginald Rose, Producers', 'film': '12 Angry Men', 'winner': False}, {'year': 1957, 'category': ['BEST MOTION PICTURE', 'SOUND RECORDING'], 'name': 'Arthur Hornblow, Jr., Producer', 'film': 'Witness for the Prosecution', 'winner': False}, {'year': 1958, 'category': ['BEST MOTION PICTURE'], 'name': 'Warner Bros.', 'film': 'Auntie Mame', 'winner': False}, {'year': 1958, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay--based on material from another medium)'], 'name': 'Lawrence Weingarten, Producer', 'film': 'Cat on a Hot Tin Roof', 'winner': False}, {'year': 1958, 'category': ['BEST MOTION PICTURE', 'WRITING (Story and Screenplay--written directly for the screen)'], 'name': 'Stanley Kramer, Producer', 'film': 'The Defiant Ones', 'winner': False}, {'year': 1958, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay--based on material from another medium)'], 'name': 'Arthur Freed, Producer', 'film': 'Gigi', 'winner': True}, {'year': 1958, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay--based on material from another medium)'], 'name': 'Harold Hecht, Producer', 'film': 'Separate Tables', 'winner': False}, {'year': 1959, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay--based on material from another medium)'], 'name': 'Otto Preminger, Producer', 'film': 'Anatomy of a Murder', 'winner': False}, {'year': 1959, 'category': ['BEST MOTION PICTURE', 'SOUND', 'SPECIAL EFFECTS', 'WRITING (Screenplay--based on material from another medium)'], 'name': 'Sam Zimbalist, Producer', 'film': 'Ben-Hur', 'winner': True}, {'year': 1959, 'category': ['BEST MOTION PICTURE'], 'name': 'George Stevens, Producer', 'film': 'The Diary of Anne Frank', 'winner': False}, {'year': 1959, 'category': ['BEST MOTION PICTURE', 'SOUND', 'WRITING (Screenplay--based on material from another medium)'], 'name': 'Henry Blanke, Producer', 'film': "The Nun's Story", 'winner': False}, {'year': 1959, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay--based on material from another medium)'], 'name': 'John Woolf and James Woolf, Producers', 'film': 'Room at the Top', 'winner': False}, {'year': 1960, 'category': ['BEST MOTION PICTURE', 'SOUND'], 'name': 'John Wayne, Producer', 'film': 'The Alamo', 'winner': False}, {'year': 1960, 'category': ['BEST MOTION PICTURE', 'SOUND', 'WRITING (Story and Screenplay--written directly for the screen)'], 'name': 'Billy Wilder, Producer', 'film': 'The Apartment', 'winner': True}, {'year': 1960, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay--based on material from another medium)'], 'name': 'Bernard Smith, Producer', 'film': 'Elmer Gantry', 'winner': False}, {'year': 1960, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay--based on material from another medium)'], 'name': 'Jerry Wald, Producer', 'film': 'Sons and Lovers', 'winner': False}, {'year': 1960, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay--based on material from another medium)'], 'name': 'Fred Zinnemann, Producer', 'film': 'The Sundowners', 'winner': False}, {'year': 1961, 'category': ['BEST MOTION PICTURE'], 'name': 'Joshua Logan, Producer', 'film': 'Fanny', 'winner': False}, {'year': 1961, 'category': ['BEST MOTION PICTURE', 'SOUND', 'SPECIAL EFFECTS', 'WRITING (Screenplay--based on material from another medium)'], 'name': 'Carl Foreman, Producer', 'film': 'The Guns of Navarone', 'winner': False}, {'year': 1961, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay--based on material from another medium)'], 'name': 'Robert Rossen, Producer', 'film': 'The Hustler', 'winner': False}, {'year': 1961, 'category': ['BEST MOTION PICTURE', 'WRITING (Screenplay--based on material from another medium)'], 'name': 'Stanley Kramer, Producer', 'film': 'Judgment at Nuremberg', 'winner': False}, {'year': 1961, 'category': ['BEST MOTION PICTURE', 'SOUND', 'WRITING (Screenplay--based on material from another medium)'], 'name': 'Robert Wise, Producer', 'film': 'West Side Story', 'winner': True}]
 
        #tested against expect answer, is not none, and no result
        self.assertEqual(x, x1)
        self.assertIsNot(x, [])
        self.assertEqual(searchByCategory("Worst", data), [])
        
    def test_year(self):
        x = searchByYear(1930, data)
        x1 = [{'year': 1930, 'category': ['ACTOR', 'ACTRESS', 'DIRECTING'], 'name': 'Lionel Barrymore', 'film': 'A Free Soul', 'winner': True}, {'year': 1930, 'category': ['ACTOR', 'DIRECTING', 'OUTSTANDING PRODUCTION', 'WRITING (Adaptation)'], 'name': 'Jackie Cooper', 'film': 'Skippy', 'winner': False}, {'year': 1930, 'category': ['ACTOR', 'ACTRESS', 'ART DIRECTION', 'CINEMATOGRAPHY', 'DIRECTING', 'OUTSTANDING PRODUCTION', 'WRITING (Adaptation)'], 'name': 'Richard Dix', 'film': 'Cimarron', 'winner': False}, {'year': 1930, 'category': ['ACTOR'], 'name': 'Fredric March', 'film': 'The Royal Family of Broadway', 'winner': False}, {'year': 1930, 'category': ['ACTOR', 'DIRECTING', 'OUTSTANDING PRODUCTION'], 'name': 'Adolphe Menjou', 'film': 'The Front Page', 'winner': False}, {'year': 1930, 'category': ['ACTRESS', 'ART DIRECTION', 'CINEMATOGRAPHY', 'DIRECTING'], 'name': 'Marlene Dietrich', 'film': 'Morocco', 'winner': False}, {'year': 1930, 'category': ['ACTRESS'], 'name': 'Marie Dressler', 'film': 'Min and Bill', 'winner': True}, {'year': 1930, 'category': ['ACTRESS', 'WRITING (Adaptation)'], 'name': 'Ann Harding', 'film': 'Holiday', 'winner': False}, {'year': 1930, 'category': ['ART DIRECTION'], 'name': 'Stephen Goosson, Ralph Hammeras', 'film': 'Just Imagine', 'winner': False}, {'year': 1930, 'category': ['ART DIRECTION', 'CINEMATOGRAPHY'], 'name': 'Anton Grot', 'film': 'Svengali', 'winner': False}, {'year': 1930, 'category': ['ART DIRECTION'], 'name': 'Richard Day', 'film': 'Whoopee!', 'winner': False}, {'year': 1930, 'category': ['CINEMATOGRAPHY'], 'name': 'Charles Lang', 'film': 'The Right to Love', 'winner': False}, {'year': 1930, 'category': ['CINEMATOGRAPHY'], 'name': 'Floyd Crosby', 'film': 'Tabu', 'winner': True}, {'year': 1930, 'category': ['OUTSTANDING PRODUCTION'], 'name': 'Fox', 'film': 'East Lynne', 'winner': False}, {'year': 1930, 'category': ['OUTSTANDING PRODUCTION'], 'name': 'Metro-Goldwyn-Mayer', 'film': 'Trader Horn', 'winner': False}, {'year': 1930, 'category': ['SOUND RECORDING', 'SOUND RECORDING', 'SOUND RECORDING', 'SOUND RECORDING'], 'name': 'Samuel Goldwyn - United Artists Studio Sound Department', 'film': 'nan', 'winner': False}, {'year': 1930, 'category': ['WRITING (Adaptation)'], 'name': 'Seton I. Miller, Fred Niblo, Jr.', 'film': 'The Criminal Code', 'winner': False}, {'year': 1930, 'category': ['WRITING (Adaptation)'], 'name': 'Francis Faragoh, Robert N. Lee', 'film': 'Little Caesar', 'winner': False}, {'year': 1930, 'category': ['WRITING (Original Story)'], 'name': 'John Monk Saunders', 'film': 'The Dawn Patrol', 'winner': True}, {'year': 1930, 'category': ['WRITING (Original Story)'], 'name': 'Rowland Brown', 'film': 'The Doorway to Hell', 'winner': False}, {'year': 1930, 'category': ['WRITING (Original Story)'], 'name': "Harry d'Abbadie d'Arrast, Douglas Doty, Donald Ogden Stewart", 'film': 'Laughter', 'winner': False}, {'year': 1930, 'category': ['WRITING (Original Story)'], 'name': 'John Bright, Kubec Glasmon', 'film': 'The Public Enemy', 'winner': False}, {'year': 1930, 'category': ['WRITING (Original Story)'], 'name': 'Lucien Hubbard, Joseph Jackson', 'film': 'Smart Money', 'winner': False}]
        
        
        #tested against expect answer, is not none, and no result
        self.assertEqual(x, x1)
        self.assertIsNot(x, [])
        self.assertEqual(searchByYear(1920, data), [])
        
             
unittest.main()      
        
