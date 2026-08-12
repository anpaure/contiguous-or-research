# Exact seam deficit for the k=15 segmented carrier

Let the rank-8 cycle factor be lower-rainbow at depth one.  Cut it into
segments and concatenate oriented segments by Johnson seams.  Write

- \(R\) for the set of lower colours of the cut cycle edges;
- \(S\) for the set of lower colours of the new seams.

Because every original lower colour occurs once, the resulting middle path
misses exactly

\[
h=|R\setminus S|
\]

rank-7 colours.  Raw slot slack is irrelevant.  A depth-three linear compiler
has only one non-canonical rank-7 slot at each end, so optimal compilation
requires \(h\le2\).

## SAT/flow encoding

For every segment item \(i\), orientation/cut option \(o\), and compatible
directed seam \(e=(i,o)\to(j,o')\), use variables \(z_{io}\) and \(x_e\).

1. Choose exactly one option per item.
2. Give every chosen option one incoming arc or the unique start flag, and
   one outgoing arc or the unique end flag.
3. Add standard reachability/subtour cuts to make the selected path connected.
4. Retain only Johnson seams whose two endpoint chronologies are depth-three
   residence-safe.
5. For each possible cut colour \(c\), let \(m_c\) mean that the selected cut
   removes \(c\) and no selected seam has colour \(c\).  Encode

   \[
   z_{io}\Longrightarrow
   \left(m_c\vee\bigvee_{e:\,\ell(e)=c}x_e\right),
   \qquad \sum_c m_c\le2.
   \]

6. Split each \(m_c\) into left/right endpoint flags.  At the left, \(c\)
   must be a rank-7 subset of the first rank-8 middle set and contain the
   coordinate deleted by the first transition.  Dually, at the right it must
   contain the coordinate inserted by the last transition.  Allow at most
   one missing colour per endpoint.
7. Upper safety is a separate coverage family: every upper interval occurrence
   destroyed by selected cuts must retain another internal occurrence or be
   recreated by a selected seam window.  The existing q1/q2 occurrence clauses
   implement this.

This exact model is implemented in
`scratch/k15_segment_splice_sat.py` via
`--max-q1-lower-deficit 2`.

## Step19 obstruction

The file `scratch/k15_dual_descent_a4_step19.segments.json` has 17 physical
cycles.  Minimum residence repair makes 23 compulsory defect cuts; cutting
each of the other 15 cycles once gives 38 segments and hence 37 seams.

The decisive portal audit is statewise.  For each of the 45 minimum-cut
solutions of the variable length-45 defect cycle, enumerate every orientation
of every defect segment, every cut/orientation of every clean cycle, and every
residence-safe Johnson seam between different segment items.  Then compare
the seam-colour palette with the 23 compulsory defect-cut colours.

Result:

| unportalable compulsory cut colours | minimum-cut solutions |
|---:|---:|
| 22 | 30 |
| 23 | 15 |

Thus every minimum-23 segmentation satisfies

\[
h=|R\setminus S|\ge22,
\]

even before path connectivity, upper safety, or endpoint compatibility are
imposed.  In the declared cut solution (solution 19), only colour 11089 has
any safe portal (four); the other 22 have none.  In solution 0, all 23 are
unportalable.

The audited data are in `scratch/k15_step19_q1_portal_floor.json`.

Therefore orienting and ordering the step19 minimum-cut segments cannot yield
an optimal k=15 compiler carrier.  The next construction must alter the local
defect cuts themselves (for example by a trade that replaces a bad cut colour
with a portalable one), add surgery that changes segment endpoints, or start
from a different cycle factor.  No global routing theorem can repair this
particular segmentation.

