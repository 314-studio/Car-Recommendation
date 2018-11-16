import wx
import pickle
from sklearn import linear_model

class mainFrame(wx.Frame):

    def __init__(self, app_title, app_size):
        wx.Frame.__init__(self, None, -1, app_title, app_size)
        panel = wx.Panel(self, -1)

        self.label_content = ['性别', '年龄', '借记卡数', '贷记卡数', '近1年消费总笔数', '近1年消费总金额', '消费城市数']
        self.box_count = 7
        self.box_height = app_size[1] / self.box_count
        self.label_width = 30
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(panel, label='请输入数据：', style=wx.ALIGN_LEFT)
        self.vbox.Add(label, proportion=0, flag=wx.EXPAND, border=10)

        self.hbox = wx.BoxSizer()
        self.vbox.Add(self.hbox, 0, wx.EXPAND, 0)

        self.init_panel(panel)

        panel.SetSizer(self.vbox)
    
    def loaf_model():
        with open('lasso_model.pickle', 'rb') as fr:
            self.reg_lasso = pickle.load(fr)
    
    def init_panel(self, panel):
        self.input_box_list = []
        grid_sizer = wx.GridSizer(self.box_count, 2, 5, 5)
        output_sizer = wx.BoxSizer(wx.VERTICAL)

        for i in range(self.box_count):
            input_label = wx.StaticText(panel, label=self.label_content[i], style=wx.ALIGN_LEFT)
            grid_sizer.Add(input_label, 0, wx.EXPAND)
            input_text_box = wx.TextCtrl(panel)
            self.input_box_list.append(input_text_box)
            grid_sizer.Add(input_text_box, 0, wx.EXPAND)
        self.hbox.Add(grid_sizer, 0, wx.ALIGN_LEFT, 0)

        self.prec_button = wx.Button(panel, -1, '开始预测', style=wx.CENTER)
        self.prec_button.Bind(wx.EVT_BUTTON, self.on_button_click)
        output_sizer.Add(self.prec_button, 0, wx.ALIGN_CENTER, 10)

        self.area_text = wx.TextCtrl(panel, -1, size=(200, 200), 
            style=(wx.TE_MULTILINE | wx.TE_DONTWRAP | wx.TE_RICH2))
        self.area_text.SetInsertionPoint(0)
        output_sizer.Add(self.area_text, 0, 0, 0)

        self.hbox.Add(output_sizer, 0, wx.ALIGN_RIGHT, 0)

    def on_button_click(self, event):
        values = []
        for input_box in self.input_box_list:
            values.append(input_box.GetValue())

if __name__ == '__main__':
    title = '模型演示'
    app = wx.App()

    frame = mainFrame(title, (400, 300))
    frame.Center()
    frame.Show()
    app.MainLoop()