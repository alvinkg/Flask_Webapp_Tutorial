from website import create_app

app = create_app()





# run app only if it is being run directly
if __name__ == "__main__":
    app.run(debug=True)
    
