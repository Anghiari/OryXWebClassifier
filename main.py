import web
import handler
import utils
import urllib2
from ml.Predict import Predict

render = web.template.render('template/')

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return render.index(url="",isValid=True)
    
    def POST(self):
        urlt = web.data().split('url=')
        urll = urllib2.unquote(urlt[1])
        if handler.checkUrl(urll):
            predtins = pred.predictBlog(urll)
            return render.results(url=urll,prediction = predtins,type=handler.getType(predtins[0].value))
        else:
            return render.index(url=urll,isValid=False)
        

if __name__ == "__main__":
    app = web.application(urls, globals())
    pred = Predict()
    app.run()