Feature: View survey data
  As a Collection Exercise Coordinator
  I need to view the survey details for all 'RRM on-boarding' surveys are stored in RM
  So that I am assured the survey details are correct

  Scenario: View all default surveys
    Given surveys exist in the system
    When the internal user views the survey page
    Then the internal user can view all surveys
      | survey_id | survey_name                                                   | survey_short_name | survey_legal_basis                  |
      | 023       | Monthly Business Survey - Retail Sales Index                  | RSI               | Statistics of Trade Act 1947        |
      | 062       | Annual Inward Foreign Direct Investment Survey                | AIFDI             | Statistics of Trade Act 1947        |
      | 063       | Annual Outward Foreign Direct Investment Survey               | AOFDI             | Statistics of Trade Act 1947        |
      | 064       | Quarterly Inward Foreign Direct Investment Survey             | QIFDI             | Statistics of Trade Act 1947        |
      | 065       | Quarterly Outward Foreign Direct Investment Survey            | QOFDI             | Statistics of Trade Act 1947        |
      | 066       | Quarterly Survey of Building Materials Sand and Gravel        | Sand & Gravel     | Statistics of Trade Act 1947 - BEIS |
      | 073       | Monthly Survey of Building Materials Concrete Building Blocks | Blocks            | Statistics of Trade Act 1947 - BEIS |
      | 074       | Monthly Survey of Building Materials Bricks                   | Bricks            | Voluntary - BEIS                    |
      | 134       | Monthly Wages and Salaries Survey                             | MWSS              | Statistics of Trade Act 1947        |
      | 137       | Public Corporations Survey                                    | PCS               | Voluntary Not Stated                |
      | 139       | Quarterly Business Survey                                     | QBS               | Statistics of Trade Act 1947        |
      | 141       | Annual Survey of Hours and Earnings                           | ASHE              | Statistics of Trade Act 1947        |
      | 199       | National Balance Sheet                                        | NBS               | Voluntary Not Stated                |
      | 225       | Outward Foreign Affiliates Statistics Survey                  | OFATS             | Statistics of Trade Act 1947        |
      | 500       | Government Research and Development Survey                    | GovERD            | GovERD                              |
      | 221       | Business Register and Employment Survey                       | BRES              | Statistics of Trade Act 1947        |