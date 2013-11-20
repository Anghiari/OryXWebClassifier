import Orange, cPickle

from FeatureCrawl import FeatureCrawl

class Predict:
    
    def predictBlog(self,urlpassed):
        url = urlpassed
        b = FeatureCrawl()
        features = b.crawl(url)
        print features
        
        siteinfoo = [features['bothCommentAndArchive'], features['bothDisandKeyInMeta'], features['divCount'], features['externalLinks'], features['forumFreqWordCount'], features['hasBlogWordInMetaData'], features['hasBlogWordInURL'], features['hasCommentBox'], features['hasFeed'], features['hasForumWordInMetaData'], features['hasForumWordInURL'], features['hasMetaDis'], features['hasMetaKeywords'], features['hasPostsArchive'], features['imgCount'], features['imgToParaRatio'], features['intLinkToExtLinkRatio'], features['internalLinks'], features['itemToListRatio'], features['largeImgCount'], features['listCount'], features['listItemCount'], features['orgFreqWordCount'], features['paraCount'], features['rowCount'], features['rowToTableRatio'], features['smallParaCount'], features['tableCount'], features['totLinks'], features['wordCount'], features['wordToParaRatio'] ]
        

#print siteinfoo
        classifier = cPickle.load(open('ml/file/oryx2_1.pck'))
        #classifier_tree = cPickle.load(open('oryx3.pck'))
        
        #print 'predictions:'


        oryx = Orange.data.Table("ml/file/dataset2.csv")
#print oryx.domain.features
#print "Attributes:", ", ".join(x for x in oryx.domain.features)
        domain = oryx.domain
        inst = Orange.data.Instance(domain,[features['bothCommentAndArchive'], features['bothDisandKeyInMeta'], features['divCount'], features['externalLinks'], features['forumFreqWordCount'], features['hasBlogWordInMetaData'], features['hasBlogWordInURL'], features['hasCommentBox'], features['hasFeed'], features['hasForumWordInMetaData'], features['hasForumWordInURL'], features['hasMetaDis'], features['hasMetaKeywords'], features['hasPostsArchive'], features['imgCount'], features['imgToParaRatio'], features['intLinkToExtLinkRatio'], features['internalLinks'], features['itemToListRatio'], features['largeImgCount'], features['listCount'], features['listItemCount'], features['orgFreqWordCount'], features['paraCount'], features['rowCount'], features['rowToTableRatio'], features['smallParaCount'], features['tableCount'], features['totLinks'], features['wordCount'], features['wordToParaRatio'], None ])

#inst = Orange.data.Instance(domain, ['False', 3, 'False', 23, 64, 119, 'False', 'False', 'True', 32, 1175, 'False', 14, 'False', 'NonBlogs'])
        print "Start:"
        print "Naive bayes:"
        prediction = classifier(inst,Orange.classification.Classifier.GetBoth)
        return prediction
        print "Type: " + prediction[0].value
        print "Probability: " 
        print prediction[1][0]
        print prediction[1][1]
        print prediction[1][2]
        #print "Decision Tree:"
        #predictionK = classifier_tree(inst,result_type=2)
        #print "Type: " + predictionK[0].value
        #print "Probability: " 
        #print predictionK[1][0]
        print "End"

