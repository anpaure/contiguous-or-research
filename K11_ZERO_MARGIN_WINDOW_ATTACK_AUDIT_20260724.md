# Independent audit of the zero-margin window attack

## Verdict

**PASS.**  I found no mathematical error in the final 41,422-byte version
of `K11_ZERO_MARGIN_WINDOW_ATTACK_20260724.md`.  In particular, the endpoint
equalities do force the claimed same-index rank-five/rank-six inclusion
matching once the two selected witness families have been fixed.  The
ordered schedules, compatibility table, Johnson forest, coordinate label
laws, zero-run formulas, five $n_5=132$ mode formulas, and endpoint parity
identity all check.

No search, enumeration, random experiment, or solver was used.  This audit
uses only the exact templates in
`K11_NONSATURATED_ONE_DEFECT_CORE_20260724.md` and direct set/window
counting.

The final text explicitly makes “canonical” relative to the fixed selected
witness families and treats the endpoint-seam case separately in item 5 of
the final normal form.  No wording correction remains necessary.

## 1. Index audit and the one-jump path

For $m$ entries, the valid indices and counts are

\[
\begin{array}{c|c|c}
\text{cell}&\text{indices}&\text{count}\\ \hline
A_i&0\le i\le m-1&m\\
B_i&0\le i\le m-2&m-1\\
C_i&0\le i\le m-3&m-2\\
T_i&0\le i\le m-4&m-3.
\end{array}
\]

There are therefore $m-4$ transitions $T_i\to T_{i+1}$, indexed by
$0\le i\le m-5$, and the overlap of transition $i$ contains
$C_{i+1}$.  Thus $H=C_s$ is on a transition exactly when
$1\le s\le m-4$, and that transition is
$T_{s-1}\to T_s$.  These are the indices used in the note; there is no
off-by-one error.

At an ordinary overlap, the intersection contains a five-set and cannot be
a six-set because the two six-set targets are distinct.  Hence its rank is
five and the transition is one Johnson swap.  At the seam,

\[
d_J=6-|T_{s-1}\cap T_s|,
\qquad
\eta=d_J-1,
\]

and $H\subseteq T_{s-1}\cap T_s$ gives
$0\le\eta\le5-\rho$.  The associated five-window is the union of those
two four-windows and has rank $7+\eta$.  All other five-windows have rank
seven.  If $H$ is an endpoint triple, it is not an overlap of two
four-windows, all $m-4$ five-windows are ordinary, and setting
$\eta=0$ is correct.  Consequently

\[
U_5=7(m-4)+\eta
\]

in every case.

The lower two Johnson levels also check: ordinary adjacent four-set pair
colors have five-set union and three-set intersection; consecutive
ordinary five-set triple colors with an ordinary middle pair have six-set
union and that four-set as intersection.  Thus the stated sliding flag path
is exact away from the listed defects.

## 2. Endpoint saturation and the perfect inclusion matching

Let the central segment be $[L,R]$, where $m=R-L+1$.  After choosing its
$m-3$ four-windows as rank-six witnesses, exactly

\[
462-(m-3)=465-m=L+(464-R)
\]

rank-six witnesses are not wholly inside the segment.  Every such interval
starts before $L$ or ends after $R$.  Distinct endpoints give capacities
$L$ and $464-R$, whose sum is already the exact number of external
witnesses.  Therefore both capacities are saturated and the two classes
are disjoint.  This proves (3.9), including the absence of a witness that
crosses the whole segment.  The length-at-most-four cap then gives the
correct suffix and prefix bounds $R-2$ and $L+2$.

The rank-five argument is lossless for the same reason.  Its selected
intervals have length at most three; the only selected witnesses wholly
inside the segment are the $m-3$ ordinary triples.  Hence it has the same
$465-m$ external count and the same saturated external slots.

The potentially delicate same-index assertion is valid.  More explicitly:

* a saturated prefix left endpoint $p<L$ has global index $j=p$ in
  both families;
* for a central triple $C_i$ before $H$, both $C_i$ and $T_i$ have
  global index $j=L+i$;
* for a central triple $C_i$ after $H$, omission of $C_s$ shifts its
  index to $j=L+i-1$, exactly the index of $T_{i-1}$; and
* a saturated suffix right endpoint $p>R$ has global index $j=p-3$ in
  both families, because each family has 462 right endpoints in 465
  positions and every slot after $R$ is occupied.

At a common prefix left endpoint, a rank-six interval must end later than
the rank-five interval: equality would give one physical interval two
different ranks, while an earlier end would put a six-set inside a
five-set.  The suffix argument is symmetric.  Thus the physical
containments are strict, the central rule uses every $T_i$ exactly once,
and $I_j\mapsto J_j$ is a genuine perfect inclusion matching of the two
complete layers.

For each coordinate $x$, 252 six-sets contain $x$, while 210 five-sets
contain it.  Inclusion prevents loss of an already present coordinate, so
exactly $252-210=42$ matching edges add $x$.  Equation (3.11) is exact.

## 3. Offset schedules and compatibility

Strict endpoint order implies that both endpoint offsets are nondecreasing
and lie in $\{0,1,2,3\}$.  The rank-five schedule is chain A with the
$12$ block empty because $h_3=h_4$:

\[
00^*01^*02^*13^*23^*33^*.
\]

Rank-six singleton states are impossible.  A central four-window has index
equal to its physical start and hence state $03$.  State $12$ is
incomparable in coordinatewise offset order with $03$, so it cannot occur
anywhere in the same monotone schedule.  The five states in (3.14) are
therefore exhaustive and correctly ordered.

For same-index states $ab$ and $cd$, physical containment is precisely
$c\le a\le b\le d$, with equality of the two intervals excluded.  Applying
this test gives exactly table (3.16).  It also gives the correctly oriented
cutpoint inequalities

\[
g_1\le h_1,
\quad g_2\le h_2,
\quad g_3\ge h_5,
\quad g_4\ge h_6,
\]

including when some blocks are empty.  Hence
$[h_2,h_5)\subseteq[g_2,g_3)$, so all central matches are rigidly in the
rank-six $03$ block.

## 4. Johnson forest and alternating path cover

Within a left-oriented rank-five state block $00,01,02$, $J_j$
physically contains both $I_j$ and $I_{j+1}$; within a right-oriented
block $13,23,33$, $J_{j+1}$ does.  The two distinct five-set targets are
therefore Johnson-adjacent and their union is the displayed six-set.

If $c$ of the six rank-five state blocks are nonempty, deleting the
$c-1$ inter-block transitions leaves $462-c$ edges in $c$ linear
components.  The matching indices used inside the blocks are injective:
a left-oriented block uses all matching sources except its final vertex,
and a right-oriented block uses all except its first.  Thus exactly one
matching edge and one six-set color are omitted per component.  This proves
the rainbow count, $1\le c\le6$, and the lower bound 456.

The coordinate identities also check directly:

* the 42-extension law splits as $f_x+d_x=42$, and the $c$ omitted
  matching edges give $\sum_xd_x=c$;
* on the $c$ component words, the binary pair-window identity is
  $q_x=210+Z_x^F-c$, while the used six-set colors give
  $q_x=252-\mu_x$; hence
  $Z_x^F=42+c-\mu_x$ and
  $\sum_xZ_x^F=462+5c$;
* for each omitted matching edge, its six-set is the disjoint union of its
  five-set source and its added coordinate, so
  $\mu_x=\sigma_x+d_x$, which yields
  $Z_x^F=f_x+c-\sigma_x$; and
* orienting every component toward its omitted-source root makes $f_x$
  exactly the number of rootward $0\to1$ transitions.  The extra zero run
  occurs exactly when the root omits $x$, agreeing with (3.23).

Expanding each forest edge through its distinct six-set union and appending
the omitted matching edge at the root covers each five-set and each six-set
once.  Singleton forest components cause no exception: they become one
matching edge.  Along the resulting path cover, the 42 matching edges that
add $x$, the $g_x$ nonmatching edges that delete $x$, and the initial
and final endpoint incidences satisfy

\[
\mu_x-\tau_x=42-g_x.
\]

This is exactly (3.24), and summing gives
$\sum_xg_x=462-c$.  The middle-level path-cover theorem is sound.

## 5. Window sums and localization of short zero runs

For one coordinate, adjoining a position to every window changes the
all-zero-window count by one for each zero run of length at least the old
window length.  Summing over eleven coordinates gives (4.1), and taking a
second difference gives (4.2).  With

\[
U_3=5(m-3)+\rho,
\quad U_4=6(m-3),
\quad U_5=7(m-4)+\eta,
\]

the note correctly obtains

\[
R^{(3)}=m+8-\rho,
\quad R^{(4)}=m+1+\eta,
\quad E_3=7-\rho-\eta.
\]

The local formulas are also exact.  A boundary two-zero run contributes
$c_0-b_0$ or $c_{m-3}-b_{m-2}$.  At an internal pair $B_i$, its
coordinates are

\[
(A_{i-1}\cap A_{i+2})\setminus B_i,
\]

whose size is $c_{i-1}+c_i-6-b_i$.  It vanishes for an ordinary
$(5,4,5)$ neighborhood.  For length three, the internal contribution at
$C_i$ is

\[
12-|T_{i-1}\cup T_i|-c_i.
\]

This vanishes ordinarily and equals $5-\rho-\eta$ at an internal seam.
The two ordinary boundaries contribute one each.  If the seam is a boundary,
its contribution is $6-\rho$ and the opposite boundary contributes one.
Thus the local ledger exactly exhausts $E_3$ in both internal and endpoint
cases.

## 6. The $n_5=133$ formulas

There are $m-3$ ordinary rank-four pairs and two seam pairs, so
$U_2=4(m-3)+s_0$.  The second-difference formula gives
$E_2=8-s_0$: three for seam type $(2,3)$ and two for $(3,3)$.  The
boundary and seam contributions listed in Section 6.1 add to exactly these
totals.  The $U_1$ constants 611 and 610 are the full rank-at-most-three
incidence 616 less missing seam ranks five and six, respectively.  Using
$m=229+r_1+r_2+r_3$ yields exactly (6.4).

For the internal $(2,3)$ seam, the neighboring ordinary triple and
four-window ranks force $L$ to be a three-set with two elements outside
$H$, and force $R$ to add a two-set $Q$ outside $H$.  The ordinary
right pair permits exactly the three forms in (6.6).  Since the exceptional
five-window is $H\cup P\cup Q$, its rank gives
$|P\cap Q|=1-\eta$.  The claimed seam-local zero run is precisely this
intersection.

For the coordinate budget, the complete rank-four point degree is 120.
Removing the $\lambda_x$ literal boundary targets and $H$, then adding
the two seam-cell incidences $h_x+i_x$, gives

\[
q_x=120-\lambda_x+i_x.
\]

The complete rank-at-most-three ideal has point degree 56.  Its two missing
seam colors have total incidence $h_x+i_x$, so

\[
o_x=56-h_x-i_x+r_x.
\]

Combining these with $q_x=o_x+Z_x-1$ gives exactly

\[
Z_x+\lambda_x+r_x=65+h_x+2i_x.
\]

Equations (7.5) and (7.6) follow algebraically with the stated signs.

## 7. All five $n_5=132$ modes

The mode lengths and defect counts agree with the source template.  For the
rank-four-carrier modes A, B, and C1, the same calculation gives
$E_2=8-s_0$ and $E_3=3-\eta$.  C0 replaces one ordinary rank-four pair
by an extra low pair of rank $r_e$, increasing $E_2$ by $4-r_e$ and
giving $12-s_0-r_e$.  In D, the two rank-two seam pairs and rank-three
seam give $E_2=2$, $E_3=4-\eta$, and
$0\le\eta\le2$.  Table (8.3) is therefore correct.

For the mode-uniform coordinate budget, the remaining complete rank-four
targets contribute

\[
q_x=120-\lambda_x-\delta_4h_x+\ell_x.
\]

All of these pair cells lie in $M_3$.  The total incidence of lower
literal entries is $56-k_x+r_x$; subtracting the single lower vertex
outside $M_3$ in B and C1 gives (8.5).  The binary pair identity then
gives (8.6).  In the rank-four-carrier modes the missing lower targets are
exactly the low-pair colors, so $k_x=\ell_x$.  In D they are the two seam
pair colors and $H$, so $k_x=\ell_x+h_x$.  Equations (8.7)--(8.8) have
the correct signs and no missing C1 term; its embedded rank-five pair and
attached vertex lie outside the defined $M_3$ segment.

For an internal C0 extra pair, the two adjacent five-sets have a four-set
intersection $K\supseteq B$.  If $|B|=2$, the rank-at-most-three outer
entries are forced to be exactly $J\cup\{a\}$ and $J\cup\{b\}$, while
nonliterality of $B$ forces the middle entries to be its two singletons.
If $|B|=3$, the displayed $K=B\cup\{j\}$ form is exhaustive and $j$
is the sole two-zero-run coordinate.  Boundary replacement by (5.1) or
(5.2) preserves the total.

In mode D, the neighboring triple ranks force $L,R$ to be three-sets,
and the four-window ranks force both to be disjoint from $H$.  Hence

\[
T_{s-1}\cap T_s=H\cup(L\cap R)
\]

has rank $3+|L\cap R|=5-\eta$, proving
$|L\cap R|=2-\eta$ and the asserted local zero-run interpretation.

## 8. Birth/death labels, parity, and final scope

For $4\le i\le m-5$, both transitions used in Section 9 exist:

\[
T_{i-4}\to T_{i-3}
\quad\text{and}\quad
T_i\to T_{i+1}.
\]

When they are ordinary swaps, the first has a unique entering coordinate in
$A_i$, absent from the preceding four entries, and the second has a unique
leaving coordinate in $A_i$, absent from the following four.  Thus the
birth/death statements, the possible loop for a rank-two entry, and the
four-zero buffers around a safe singleton are all correct.

For coordinate $x$, zero runs of length at least four in the entry word
are in bijection with zero runs in its $T$-membership word.  An internal
run creates two changes; a run touching the left or right endpoint loses
the corresponding change.  This proves

\[
\deg_x=2R_x^{(4)}-\epsilon_x^L-\epsilon_x^R.
\]

Summing uses five omissions at each endpoint and gives
$2(m-4+\eta)$, exactly twice the total Johnson distance of the
$m-4$ transitions.  The coordinatewise parity is precisely the endpoint
membership parity.  No additional contradiction follows without fixing
the endpoint six-sets, as the note states.

The final normal form accurately summarizes what was proved and does not
overclaim a contradiction or an existence theorem.
