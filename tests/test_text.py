from crawler.crawler.pipelines import CleaningItemPipeline
def test_cleaning_item_pipeline():
    text = "   This is a test string.   "
    text_after_cleaning = CleaningItemPipeline().cleaned_data(text)
    assert text_after_cleaning == "This is a test string."
def test_cleaning_item_pipeline_with_multiple_spaces():
    content = "   This is a test string with    multiple spaces.   "
    content_after_cleaning = CleaningItemPipeline().cleaned_data(content)
    assert content_after_cleaning == "This is a test string with multiple spaces."