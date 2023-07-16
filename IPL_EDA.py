import streamlit as st
import pandas as pd
import plotly.express as px

# load the data
x1 = pd.read_csv('ipl_cleaned_data.csv')
p = pd.read_csv('IPL_Data.csv')
p1 = pd.read_csv('Final_ipl_data.csv')
p2 = pd.read_csv('orange_cap.csv', index_col='Unnamed: 0')
p2.drop(['Ball Faced'], inplace=True, axis=1)
p3 = pd.read_excel('purplecap.xlsx')
data7 = pd.read_csv('ipl_matches.csv')
data6 = pd.read_csv('mat_info.csv')

# Heading
st.subheader("Game of Analytics: Cricketing Insights from IPL")
st.sidebar.image("img.png")
st.sidebar.title("Cricketing Insights from IPL")

years = ['Select Year', 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
teams = ['Select Team', 'Chennai Super Kings', 'Delhi Capitals', 'Gujarat Titans', 'Kolkata Knight Riders',
         'Lucknow Super Giants',
         'Mumbai Indians',
         'Royal Challenger Bangalore', "Rajasthan Royals", 'Sunrise Hyderabad'
         ]
pp = p1['batter'].unique()
performance = ['Select cap', 'Orange Cap', 'Purple Cap']
# button for history
ipl_history = st.sidebar.button('IPL History')
seasons = st.sidebar.selectbox("Seasons", years)
s1 = st.sidebar.button('Season Insight')

t1 = st.sidebar.selectbox("Teams", teams)
s2 = st.sidebar.button('Teams Insights')

tt = st.sidebar.selectbox("Player Insights", pp)
ss = st.sidebar.button("Player's Performance")

performance = st.sidebar.selectbox('Batters / Bowlers', performance)
s3 = st.sidebar.button('Performance')


# function

def season(y):
    st.write("Matches won by each team in season", y)
    df = x1[x1['Year'] == y]
    df = df.value_counts('Won')
    df = df.reset_index().rename(columns={0: 'Count', 'Won': 'Team Name'})
    fig = px.bar(df, x='count', y='Team Name', color_discrete_sequence=['light Blue'] * len(df),
                 labels={'x': 'Some X', 'y': 'Some Y'})
    st.plotly_chart(fig)

    st.write("Matches held by each Stadium in season", y)
    df1 = x1[x1['Year'] == y]
    df1 = df1.value_counts('Stadium')
    df1 = df1.reset_index().rename(columns={0: 'Total Count', 'Stadium': 'Stadium Name'})
    fig1 = px.bar(df1, x='count', y='Stadium Name', color_discrete_sequence=['light blue'] * len(df1),
                  labels={'x': 'Some X', 'y': 'Some Y'})
    st.plotly_chart(fig1)

    st.write("Top 10 Batsman who scored highest runs in Season", y)
    x3 = p1[p1['Season'] == y]
    x3 = x3.groupby('batter')['batsman_run'].sum().sort_values(ascending=False).reset_index().head(10)
    fig2 = px.bar(x3, x='batsman_run', y='batter', color_discrete_sequence=['light blue'] * len(x3),
                  labels={'x': 'Some X', 'y': 'Some Y'})
    st.plotly_chart(fig2)

    st.write("Top 10 Bowler who took highest wicket in Season", y)
    x3 = p1[p1['Season'] == y]
    x3 = x3.groupby('bowler')['isWicketDelivery'].sum().sort_values(ascending=False).reset_index().head(10)
    fig2 = px.bar(x3, x='isWicketDelivery', y='bowler', color_discrete_sequence=['light blue'] * len(x3),
                  labels={'x': 'Some X', 'y': 'Some Y'})
    st.plotly_chart(fig2)

    st.write('Composition of Toss Decision', y)
    df2 = p[p['Season'] == y]
    df2 = df2.value_counts('TossDecision')
    df2 = df2.reset_index().rename(columns={0: 'Total', 'TossDecision': 'Toss Decision'})
    fig2 = px.pie(df2, values='count', names='Toss Decision')
    st.plotly_chart(fig2)

    st.write('Composition of Won By', y)
    df3 = p[p['Season'] == y]
    df3 = df3.value_counts('WonBy')
    df3 = df3.reset_index().rename(columns={0: 'count', 'WonBy': 'WonBy'})
    fig3 = px.pie(df3, values='count', names='WonBy')
    st.plotly_chart(fig3)

    st.write("Top 10 batter who smashed more fours", y)
    s = p1[p1['Season'] == y]
    s = s[s['batsman_run'] == 4]
    s = s.groupby('batter')['batsman_run'].count().sort_values(ascending=False).reset_index().rename(
        columns={'batsman_run': 'Total_fours'}).head(10)
    fig2 = px.bar(s, x='Total_fours', y='batter')
    st.plotly_chart(fig2)

    st.write("Top 10 batter who smashed more sixes", y)
    s6 = p1[p1['Season'] == y]
    s6 = s6[s6['batsman_run'] == 6]
    s6 = s6.groupby('batter')['batsman_run'].count().sort_values(ascending=False).reset_index().rename(
        columns={'batsman_run': 'Total_sixes'}).head(10)
    fig2 = px.bar(s6, x='Total_sixes', y='batter')
    st.plotly_chart(fig2)

    st.write('Top 10 Players who won the most Man of the Match in season', y)
    df4 = p[p['Season'] == y]
    df4 = df4.value_counts('Player_of_Match')
    df4 = df4.reset_index().rename(columns={0: 'count'}).head(10)
    fig4 = px.bar(df4, x='count', y='Player_of_Match')
    st.plotly_chart(fig4)

    col1, col2 = st.columns(2)
    with col1:
        st.write("Total Fours are smashed in Season", y)
        data3 = p1[p1['Season'] == y]
        data3 = data3[data3['batsman_run'] == 4]
        data3 = data3['batsman_run'].count()
        st.write("Total Fours ", data3)

    with col2:
        st.write("Total Sixes are smashed in Season", y)
        data3 = p1[p1['Season'] == y]
        data3 = data3[data3['batsman_run'] == 6]
        data3 = data3['batsman_run'].count()
        st.write("Total Sixes ", data3)


# team def function

def team(team1):
    st.write("Top 10 Batter ", team1)
    csk1 = p1[(p1['Team1'] == team1) | (p1['Team2'] == team1)]
    csk1 = csk1.groupby('batter')['batsman_run'].sum().sort_values(ascending=False).head(10)
    csk1 = csk1.reset_index()
    fig6 = px.bar(csk1, x='batsman_run', y='batter', color_discrete_sequence=['orange'] * len(csk1),
                  labels={'x': 'Some X', 'y': 'Some Y'})
    st.plotly_chart(fig6)

    st.write("Top 10 Bowler ", team1)
    csk = p1[(p1['Team1'] == team1) | (p1['Team2'] == team1)]
    csk = csk.groupby('bowler')['isWicketDelivery'].sum().sort_values(ascending=False).head(10)
    csk = csk.reset_index()
    fig0 = px.bar(csk, x='isWicketDelivery', y='bowler', color_discrete_sequence=['purple'] * len(csk),
                  labels={'x': 'Some X', 'y': 'Some Y'})
    st.plotly_chart(fig0)

    st.write("How Many matches they won in each stadium by", team1)
    g = data7[data7['WinningTeam'] == team1]
    g = g.groupby('Venue')['WonBy'].count().reset_index().rename(
        columns={'WonBy': 'How Many matches they won in each stadium'})
    fig3 = px.bar(g, x='How Many matches they won in each stadium', y='Venue')
    st.plotly_chart(fig3)

    st.write("Reached in Top 4 placed ", team1)
    b = data7[data7['WinningTeam'] == team1]
    b = b[(b['MatchNumber'] == 'Final') | (b['MatchNumber'] == 'Qualifier 2') | (b['MatchNumber'] == 'Qualifier 1') | (
            b['MatchNumber'] == 'Eliminator') | (b['MatchNumber'] == 'Elimination Final') | (
                  b['MatchNumber'] == '3rd Place Play-Off')
          | (b['MatchNumber'] == 'Semi Final')]
    b = b.groupby('MatchNumber')['ID'].count().reset_index().rename(columns={'ID': 'Total Number of times'})
    fig1 = px.bar(b, x='MatchNumber', y='Total Number of times')
    st.plotly_chart(fig1)

    st.write(team1, "Won by ")
    g = data7[data7['WinningTeam'] == team1]
    g = g.groupby(['WinningTeam', 'WonBy'])['ID'].count().reset_index().rename(columns={'ID': 'Total'})
    fig1 = px.pie(g, values='Total', names='WonBy')
    st.plotly_chart(fig1)

    col1, col2 = st.columns(2)
    with col1:
        st.write("Total Fours are smashed by", team1)

        final = p1[(p1['Team1'] == team1) | (p1['Team2'] == team1)]
        final = final[final['batsman_run'] == 4]
        final = final['batsman_run'].count()
        st.write("Total 4's", final)

    with col2:
        st.write("Total Sixes are smashed by", team1)

        final = p1[(p1['Team1'] == team1) | (p1['Team2'] == team)]
        final = final[final['batsman_run'] == 6]
        final = final['batsman_run'].count()
        st.write("Total 6's", final)


# player def function

def player(y1):
    v = p1[p1['batter'] == y1]
    v = v.groupby('Season')['batsman_run'].sum().reset_index()
    fig1 = px.bar(v, x='Season', y='batsman_run', color_discrete_sequence=['white'] * len(v),
                  labels={'x': 'Some X', 'y': 'Some Y'})
    st.plotly_chart(fig1)

    st.write("Total 4s in each year by", y1)
    v = p1[p1['batter'] == y1]
    v = v[v['batsman_run'] == 4]
    v = v.groupby('Season')['batsman_run'].count().reset_index().rename(columns={'batsman_run': 'Total 4s'})
    fig1 = px.bar(v, x='Season', y='Total 4s', color_discrete_sequence=['orange'] * len(v),
                  labels={'x': 'Some X', 'y': 'Some Y'})
    st.plotly_chart(fig1)

    st.write("Total 6s in each year by", y1)
    v = p1[p1['batter'] == y1]
    v = v[v['batsman_run'] == 6]
    v = v.groupby('Season')['batsman_run'].count().reset_index().rename(columns={'batsman_run': 'Total 6s'})
    fig1 = px.bar(v, x='Season', y='Total 6s', color_discrete_sequence=['green'] * len(v),
                  labels={'x': 'Some X', 'y': 'Some Y'})
    st.plotly_chart(fig1)

    st.write("How much total runs Scored When Opponent team won by", y1)
    v = data6[data6['batter'] == y1]
    v = v.groupby(['batter', 'WinningTeam'])['batsman_run'].sum().reset_index().rename(columns={'WinningTeam': 'Team'})
    v = v[['Team', 'batsman_run']]
    fig1 = px.bar(v, x='batsman_run', y='Team', color_discrete_sequence=['light blue'] * len(v),
                  labels={'x': 'Some X', 'y': 'Some Y'})
    st.plotly_chart(fig1)

    st.write(" How much Strike Rate When opponent team won by", y1)
    v = data6[data6['batter'] == y1]
    s = v.groupby(['batter', 'WinningTeam'])['batsman_run'].sum().reset_index().rename(columns={'WinningTeam': 'Team'})
    s11 = v.groupby(['batter', 'WinningTeam'])['ballnumber'].count().reset_index().rename(
        columns={'WinningTeam': 'Team', 'ballnumber': 'ballfaced'})
    s['ballfaced'] = s11['ballfaced']
    s['strikerate'] = round(s['batsman_run'] / s['ballfaced'] * 100, 2)
    s = s[['Team', 'strikerate']]
    fig1 = px.bar(s, x='Team', y='strikerate', color_discrete_sequence=['light blue'] * len(v),
                  labels={'x': 'Some X', 'y': 'Some Y'})
    st.plotly_chart(fig1)

    st.write("Runs scored by first innings(field)/second innings(bat) by", y1)
    v = data6[data6['batter'] == y1]
    td = v.groupby(['batter', 'TossDecision'])['batsman_run'].sum().reset_index()

    td = td[['TossDecision', 'batsman_run']]
    fig1 = px.pie(td, names='TossDecision', values='batsman_run')
    st.plotly_chart(fig1)


if ipl_history:
    st.write("The Indian Premier League (IPL) is a popular annual men's Twenty20 (T20) cricket league held in India. "
             "Founded by the BCCI in 2007, it features ten franchise teams representing different cities. The IPL is "
             "held between March and May each year and has its dedicated window in the ICC Future Tours Programme.The "
             "IPL is widely regarded as the most popular cricket league globally and has consistently attracted large "
             "crowds. It achieved various milestones, including being the first sporting event to be live-streamed on "
             "YouTube in 2010. The IPL has a significant brand value, reaching billions of dollars in 2022. It also "
             "contributes substantially to India's economy, with the 2015 season alone adding millions of dollars to "
             "the country's GDP.In recent years, the IPL's value has soared, with its estimated worth surpassing $10 "
             "billion in 2022."
             "Chennai Super Kings emerged as the champions in the IPL 2023, defeating the Gujarat Titans in the final "
             "at the Narendra Modi Stadium in Ahmedabad")
    st.write("The league's popularity extends to digital platforms, with the 2023 final being the "
             "most-streamed live event, drawing millions of viewers.In 2023, the IPL sold its media rights for a "
             "staggering $6.4 billion for the period of 2023–2027, further solidifying its financial success.")

    st.subheader('Background')
    st.write("The Indian Cricket League (ICL) was established in 2007 with financial backing from Zee Entertainment "
             "Enterprises. However, it did not receive recognition from the Board of Control for Cricket in India ("
             "BCCI) or the International Cricket Council (ICC). The BCCI was unhappy with its committee members "
             "joining the ICL's executive board.To discourage players from joining the ICL, the BCCI took measures "
             "such as increasing the prize money in its domestic tournaments. Additionally, the BCCI imposed lifetime "
             "bans on players who associated themselves with the ICL. The BCCI considered the ICL as a rebel league, "
             "as it operated outside the framework and approval of the official cricketing bodies.UserFoundationOn 13 "
             "September 2007,[20] following India's victory at the 2007 T20 World Cup,[21] the BCCI announced a "
             "franchis")
    st.subheader("Foundation")
    st.write("The Indian Premier League (IPL) was founded on September 13, 2007, by the Board of Control for Cricket "
             "in India (BCCI) after India's victory in the 2007 T20 World Cup. It was announced as a franchise-based "
             "Twenty20 cricket competition. Lalit Modi, the BCCI vice-president, led the IPL initiative and provided "
             "details about the tournament's format, prize money, franchise system, and squad composition rules. The "
             "IPL was not a knee-jerk reaction to the rival Indian Cricket League (ICL) but had been in the works for "
             "two years.An auction was held on January 24, 2008, to select team owners for the IPL franchises. The "
             "winning bidders and the cities where the teams would be based were announced, including Bangalore, "
             "Chennai, Delhi, Hyderabad, Jaipur, Kolkata, Mohali, and Mumbai. The franchises were sold for a total of "
             "$723.59 million.Due to Pakistan's involvement in the 2008 Mumbai terrorist attacks, Pakistani players "
             "have not been allowed to participate in the IPL since then. Additionally, the ICL, which was a private "
             "T20 league and a competitor to the IPL, shut down in 2009 due to the ban imposed on players choosing to "
             "participate in it.")
    st.subheader("Expansion and Termination")
    st.write("The Indian Premier League (IPL) has seen expansions and terminations of franchises throughout its "
             "history. In 2010, Pune Warriors India and Kochi Tuskers Kerala joined the league as new franchises. "
             "However, Kochi Tuskers Kerala was terminated in 2011 due to their failure to pay the required bank "
             "guarantee. "
             "The Deccan Chargers, the 2009 champions, were terminated in 2012 after failing to find new owners. The "
             "franchise was replaced by Sunrisers Hyderabad, owned by Sun TV Network.Pune Warriors India withdrew "
             "from the IPL in 2013 over financial differences with the BCCI, and their franchise was officially "
             "terminated. "
             "In 2015, two-time champions Chennai Super Kings and Rajasthan Royals were suspended for two seasons due "
             "to their involvement in a spot-fixing and betting scandal. Rising Pune Supergiant and Gujarat Lions "
             "replaced them for the suspended seasons.Due to the COVID-19 pandemic, the 2020 season was moved to the "
             "United Arab Emirates. "
             "In 2022, the BCCI announced the addition of two new franchises for the 2022 season. RPSG Group and CVC "
             "Capital won bids for the teams, and they were named Lucknow Super Giants and Gujarat Titans.Many IPL "
             "team owners have expanded their business interests by purchasing teams in other leagues around the "
             "world, such as the South African SA20 and the Caribbean Premier League (CPL), often branding them with "
             "similar names to their IPL teams.")
if s1:
    if seasons == 2008:
        season(seasons)

    if seasons == 2009:
        season(seasons)

    if seasons == 2010:
        season(seasons)

    if seasons == 2011:
        season(seasons)

    if seasons == 2012:
        season(seasons)

    if seasons == 2013:
        season(seasons)

    if seasons == 2014:
        season(seasons)

    if seasons == 2015:
        season(seasons)

    if seasons == 2016:
        season(seasons)

    if seasons == 2017:
        season(seasons)

    if seasons == 2018:
        season(seasons)

    if seasons == 2019:
        season(seasons)

    if seasons == 2020:
        season(seasons)

    if seasons == 2021:
        season(seasons)

    if seasons == 2022:
        season(seasons)

if s2:
    if t1 == 'Chennai Super Kings':
        team(t1)
    if t1 == 'Delhi Capitals':
        team(t1)
    if t1 == 'Gujarat Titans':
        team(t1)
    if t1 == 'Kolkata Knight Riders':
        team(t1)
    if t1 == 'Lucknow Super Giants':
        team(t1)
    if t1 == 'Mumbai Indians':
        team(t1)
    if t1 == 'Royal Challengers Bangalore':
        team(t1)
    if t1 == 'Rajasthan Royals':
        team(t1)

    if t1 == 'Sunrisers Hyderabad':
        team(t1)

if s3:
    st.write("Orange Cap Information in each year")
    if performance == 'Orange Cap':
        st.dataframe(p2)

    st.write("Purple Cap Information in each year")
    if performance == 'Purple Cap':
        st.dataframe(p3)

if ss:
    if tt in pp:
        player(tt)
