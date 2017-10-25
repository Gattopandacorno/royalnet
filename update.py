import db
import errors
import time

# Stop updating if Ctrl-C is pressed
try:
    # Update Steam
    print("STEAM")
    for user in db.session.query(db.Steam).all():
        print(f"Updating {user.royal.username}", end="\t\t", flush=True)
        try:
            user.update()
        except errors.RequestError:
            print("Request Error")
        except errors.NotFoundError:
            print("Not Found Error (?)")
        else:
            print("OK")
        finally:
            time.sleep(0.5)
    # Update Rocket League
    print("ROCKET LEAGUE")
    for user in db.session.query(db.RocketLeague).all():
        print(f"Updating {user.steam.royal.username}", end="\t\t", flush=True)
        try:
            user.update()
        except errors.RequestError:
            print("Request Error")
        except errors.NotFoundError:
            print("Not Found Error (?)")
        else:
            print("OK")
        finally:
            time.sleep(0.5)
    # Update Dota 2
    print("DOTA 2")
    for user in db.session.query(db.Dota).all():
        print(f"Updating {user.steam.royal.username}", end="\t\t", flush=True)
        try:
            user.update()
        except errors.RequestError:
            print("Request Error")
        except errors.NotFoundError:
            print("Not Found Error (?)")
        else:
            print("OK")
        finally:
            time.sleep(0.5)
    # Update League of Legends
    print("LEAGUE OF LEGENDS")
    for user in db.session.query(db.LeagueOfLegends).all():
        print(f"Updating {user.royal.username}", end="\t\t", flush=True)
        try:
            user.update()
        except errors.RequestError:
            print("Request Error")
        except errors.NotFoundError:
            print("Not Found Error (?)")
        else:
            print("OK")
        finally:
            time.sleep(0.5)
    # Update Osu!
    print("OSU!")
    for user in db.session.query(db.Osu).all():
        print(f"Updating {user.royal.username}", end="\t\t", flush=True)
        try:
            user.update()
        except errors.RequestError:
            print("Request Error")
        except errors.NotFoundError:
            print("Not Found Error (?)")
        else:
            print("OK")
        finally:
            time.sleep(0.5)
    # Update Overwatch
    print("OVERWATCH")
    for user in db.session.query(db.Overwatch).all():
        print(f"Updating {user.royal.username}", end="\t\t", flush=True)
        try:
            user.update()
        except errors.RequestError:
            print("Request Error")
        except errors.NotFoundError:
            print("Not Found Error (?)")
        else:
            print("OK")
        finally:
            time.sleep(0.5)
except KeyboardInterrupt:
    pass
finally:
    print("Committing...\t\t")
    db.session.commit()
    print("OK")
    db.session.close()