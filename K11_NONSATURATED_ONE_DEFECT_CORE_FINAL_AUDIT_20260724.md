# Final audit of the nonsaturated one-defect core

Audited document:

K11_NONSATURATED_ONE_DEFECT_CORE_20260724.md

Date: 2026-07-24.

This is a proof audit only.  No finite search, solver, programmatic
enumeration, or web source was used.  The additions were checked by direct
counting, endpoint arguments, path-antichain arguments, and coordinatewise
window identities.

## 1. Final verdict

The new structural mathematics passes, subject to the corrections listed in
Section 9 below.

More precisely:

1. The zero-margin branch is correctly eliminated at \(n_5=134\).
2. The \(n_5=133\) double filtration, including its pair and triple ledgers,
   rank-six saturation, zero-run formulas, and local seam forms, is correct.
3. The five \(n_5=132\) modes are exhaustive for the coarse data
   \((x_4,s_3,\rho,t_\ast,g)\).  Their displayed numerical rows and their
   cell-family descriptions are correct.  Necessary ranges for \(n_4\)
   should be added.
4. The chain-B zero-margin analogues, recursive normal form, top-slice
   artificial-concatenation argument, rank-six saturation, and zero-run
   identities are correct.  Chain C is obtained by physical reversal.
5. The endpoint-antichain proof really does force every four-window in each
   stated physical lower segment to be a distinct selected rank-six
   witness.  There is no hidden endpoint double charge.
6. All newly displayed algebraic identities checked below have the stated
   constants.
7. An earlier draft contained one invalid attribution in Section 7.2:
   equations (7.11)--(7.14) alone do not force
   \(\Delta_3+n_4=100\) at \(n_5=134\).  The current audited text has been
   patched correctly: those rows give only
   \(\Delta_3+n_4\le100\), while equality is explicitly attributed to the
   exact boundary--core rigidity established in Section 7.1.  No invalid
   inference remains at that passage.
8. The phrases “classify” and “finite exact parameterization” must be read
   in the forward, word-to-data sense.  The rows are lossless necessary
   normal forms.  They are not converses asserting that every numerical row
   has a compatible labelled OR realization.

No new argument in the audited additions proves that a length-\(465\)
universal word is impossible, and the source correctly does not claim that
it does.

The audit is conditional on the previously established inputs used by the
source: named-cell shortening through rank four, the one-defect path
theorem, the rank-four surplus-component theorem, exact rank-four
boundary--core rigidity, and the coordinate-transversal theorem.  Section 2
of the source should list all of these; its present assertion that only four
inputs are used is incomplete.

## 2. Two structural lemmas used repeatedly

### Lemma 2.1: endpoint-antichain four-window saturation

Let a word have \(465\) positions, and select one interval witness for each
of the \(462=\binom{11}{6}\) distinct rank-six targets.  Then:

1. the selected intervals form an inclusion antichain;
2. their left endpoints are all distinct, and their right endpoints are all
   distinct;
3. every selected interval has physical length at most four.

If \(J\) is an actual contiguous segment of length \(L\ge4\), at least
\(L-3\) of the selected rank-six intervals are contained in \(J\).
Consequently, if every subinterval of \(J\) of length at most three has
OR-rank at most five, every four-window of \(J\) is a selected witness for a
distinct rank-six target.

#### Proof

If selected intervals \(I\subsetneq I'\), then
\(\operatorname{OR}(I)\subseteq\operatorname{OR}(I')\).  Both selected
values have size six, so they would be equal, contrary to the fact that the
intervals were selected for distinct targets.  Thus the family is an
antichain.  Equal left endpoints or equal right endpoints would make two
intervals comparable, proving endpoint distinctness.

Order the intervals by increasing left endpoint:
\[
 I_j=[\ell_j,r_j],\qquad 1\le j\le462.
\]
The antichain property makes the right endpoints increase in the same
order.  In one-based position notation,
\[
 \ell_j\ge j,\qquad
 r_j\le465-(462-j)=j+3.
\]
Hence \(r_j-\ell_j+1\le4\).

Write \(J=[a,b]\), so \(L=b-a+1\).  Charge a selected interval not contained
in \(J\) to its left endpoint if that endpoint is before \(a\); otherwise
charge it to its right endpoint, which must be after \(b\).  Endpoint
distinctness bounds the two classes by
\[
 (a-1)+(465-b)=465-L.
\]
Therefore at least
\[
 462-(465-L)=L-3
\]
selected intervals lie in \(J\).  Under the short-cell hypothesis, each
contained rank-six witness has length four.  There are exactly \(L-3\)
four-windows, so all of them occur, once each, and their target values are
distinct.  ∎

This proof validates every use of four-window saturation in (6.1b6),
(6.3), the five \(n_5=132\) modes, (7.6c), and the top chain-B component.
The symbol \(x_3\) used in (6.1b6) and (7.6c) is not defined in the source;
it should be defined as the number of selected rank-six witnesses having
physical length four.

### Lemma 2.2: restricted-segment zero-run identity

Fix an actual segment \(J\) of length \(L\).  For \(1\le\ell\le L\), let
\(U_\ell\) be the sum of the OR-ranks of all length-\(\ell\) windows in
\(J\).  For each coordinate, restrict its binary trace to \(J\), and count
maximal zero runs in that restricted trace, including runs truncated by an
endpoint of \(J\).  A coordinate absent from all of \(J\) contributes one
zero run of length \(L\).  Let \(R^{(\ell)}\) be the total number, over the
eleven coordinates, of these zero runs having length at least \(\ell\).
For \(1\le\ell<L\),
\[
 U_{\ell+1}-U_\ell=R^{(\ell)}-11.                 \tag{2.1}
\]

#### Proof

For one coordinate, let its restricted zero runs have lengths \(r_i\).
The number of all-zero length-\(\ell\) windows is
\[
 Z_\ell=\sum_i\max(r_i-\ell+1,0).
\]
Thus
\[
 Z_\ell-Z_{\ell+1}
   =\#\{i:r_i\ge\ell\}.
\]
The total number of length-\(\ell\) windows decreases by one when
\(\ell\) is increased to \(\ell+1\).  Therefore the increase in the number
of windows containing the coordinate is the last displayed run count minus
one.  Summing over eleven coordinates gives (2.1).  ∎

The word “restricted” is essential.  If \(R^{(\ell)}\) is interpreted using
global zero runs in the full \(465\)-position word, (6.4) and all formulas
derived from it need not hold.

## 3. Chain-A zero-margin normal form

Assume the chain-A hypotheses and
\[
 D=y_2-(93+n_5+\Delta_{\rm lit})=0.
\]
Put
\[
 p=95+n_5+\Delta_{\rm lit},\qquad L=p+1.
\]
The middle lower-pair segment has \(p\) edges and \(L\) vertices.  Its
\(p-1\) transitions consist of one carrier triple \(H\), of rank
\(\rho\in\{3,4\}\), and
\[
 p-2=93+n_5+\Delta_{\rm lit}=y_2
\]
distinct selected rank-five triples.  This confirms all constants in
(6.1a)--(6.1b).

### 3.1 The recursive pair ledger

At zero margin,
\[
 y_1=369-2n_5-\Delta_{\rm lit},
 \qquad
 \Delta_{\rm lit}=x_4+\Delta_3.
\]
After deleting the \(n_4\) literal rank-four positions, the
rank-at-most-three components have \(N-n_4\) vertices and
\[
 (N-n_4)-s_3
\]
internal pairs.  Of the \(N-1\) physical pairs of the original core,
exactly
\[
 (N-1)-[(N-n_4)-s_3]=n_4+s_3-1
\]
are not internal to a lower component.  Equality in the zero-margin pair
injection makes all of these selected rank-five pairs.  Hence the number of
rank-five pairs embedded inside lower components is
\[
\begin{aligned}
 g
   &:=y_1-(n_4+s_3-1)\\
   &=370-2n_5-s_3-x_4-\Delta_3-n_4
   \ge0.                                         \tag{3.1}
\end{aligned}
\]
This proves (6.1h).  Rearranging (3.1), and using
\(v_4+w_3=1\), gives
\[
 \Delta_3+n_4+g
   =369-2n_5-s_3-x_4+v_4+w_3,                    \tag{3.2}
\]
which is exactly (6.1i).

Let
\[
 T=135-n_5-x_4=\sum_j t_j
\]
be the total rank-four component slack, and let \(t_\ast\) be the slack of
the component containing the middle segment.  The two seam pairs below
\(H\) are not selected rank-four pair witnesses.

If \(\rho=4\), \(H\) itself is the component's one rank-four triple
witness, so the number of its pairs not selected at rank four is
\(t_\ast\).  If \(\rho=3\), all rank-four witnesses are pairs, so that
number is \(t_\ast-1\).  Therefore
\[
 \rho=4\Longrightarrow t_\ast\ge2,\qquad
 \rho=3\Longrightarrow t_\ast\ge3.                \tag{3.3}
\]
This verifies (6.1j).

Every nonliteral rank-four witness is in the central component.  Every
satellite therefore has \(q_j=0\), and the satellites have total length
\(T-t_\ast\).  Their internal pairs are all selected at rank five, so
\[
 g_{\rm sat}=T-t_\ast-(s_3-1).                    \tag{3.4}
\]
Put \(g_c=g-g_{\rm sat}\).  Counting the central pair cells not selected at
ranks four or five, and including \(H\) itself when \(\rho=3\), gives the
number \(k\) of nonliteral masks of ranks at most three:
\[
 k=t_\ast-g_c=T-s_3+1-g,\qquad
 z_1+z_2+z_3=231-k.                               \tag{3.5}
\]
Thus (6.1k) is correct in both carrier ranks.

For a formal normal-form statement the following implicit feasibility
conditions should be displayed:
\[
\begin{gathered}
 T-t_\ast\ge s_3-1,\qquad
 g_{\rm sat}\ge0,\qquad
 g\ge g_{\rm sat},\qquad g_c\ge0,\\
 k\ge2\quad(\rho=4),\qquad
 k\ge3\quad(\rho=3).
\end{gathered}                                    \tag{3.6}
\]
The last two bounds follow because the two seam colors are distinct
nonliteral lower masks, while a rank-three \(H\) is a third nonliteral mask
of a different rank.

The middle segment really is contained in one rank-at-most-three component.
If one of its physical vertices had a literal rank-four value \(R\), an
incident middle edge color \(B\) would satisfy \(R\subseteq B\) and
\(|B|\le4\), forcing \(B=R\).  This contradicts the fact that every middle
edge color is a nonliteral target.  Thus no hidden rank-four literal splits
the segment.

The topology stated after (6.1k) follows: the central component is the
\(L\)-vertex middle segment with exactly \(g_c\) low tail vertices attached
through rank-five pair edges, and the other \(s_3-1\) components are
rank-five-pair paths of total length \(T-t_\ast\).

### 3.2 Four-windows and zero runs

Every cell of length at most three in the middle segment has rank at most
five.  Lemma 2.1 therefore gives
\[
 x_3\ge L-3=p-2=y_2,                              \tag{3.7}
\]
after \(x_3\) is defined as above.  In fact every middle four-window is a
selected witness for a different rank-six target.

Let \(R_{\rm pair}=U_2\).  The exact pair/triple/four-window ledger gives
\[
\begin{aligned}
 U_2&=R_{\rm pair},\\
 U_3&=5(L-3)+\rho,\\
 U_4&=6(L-3).
\end{aligned}
\]
Lemma 2.2 yields
\[
\begin{aligned}
 R^{(2)}&=5L-4+\rho-R_{\rm pair},\\
 R^{(3)}&=L+8-\rho,\\
 \#\{\text{zero runs of exact length }2\}
   &=R^{(2)}-R^{(3)}
     =4L-12+2\rho-R_{\rm pair}.                  \tag{3.8}
\end{aligned}
\]
Each five-window contains two distinct rank-six four-window values, whose
union has rank at least seven.  Hence
\[
 U_5\ge7(L-4)
\]
and
\[
 R^{(4)}=U_5-U_4+11\ge L+1.
\]
It follows that the number of exact length-three zero runs is at most
\[
 R^{(3)}-R^{(4)}\le7-\rho.
\]
All identities in (6.1b7) are therefore correct.

### 3.3 Adjacent-rank separation

At every transition other than the seam, the two edge colors \(B_i,B_{i+1}\)
have union rank five and contain the nonempty shared physical entry in their
intersection.  Thus
\[
 |B_i|+|B_{i+1}|
   =5+|B_i\cap B_{i+1}|\ge6.                     \tag{3.9}
\]
This verifies (6.1c).  Since every middle edge color has rank two, three, or
four, a rank-two color can have only rank-four neighbors away from the
seam.  Deleting the seam transition leaves at most two paths.  On each
path, rank-two vertices are separated by rank-four vertices, so
\[
 p_2\le p_4+2.                                   \tag{3.10}
\]
This proves (6.1d).

The advertised sharpenings also pass.  For a rank-four seam of type
\((2,3)\) or \((3,2)\), only one of the two resulting paths ends at a
rank-two seam color, so only that path can have one more rank-two than
rank-four vertex; hence \(p_2\le p_4+1\).  For seam type \((3,3)\), neither
path ends at a rank-two seam color, and \(p_2\le p_4\).  A rank-three seam
has two rank-two seam colors and retains the general \(+2\) bound.

### 3.4 Incidence ceiling

Let the middle edge colors be \(B_1,\ldots,B_p\), with ranks counted by
\(p_2,p_3,p_4\), and put
\[
 R_{\rm pair}=2p_2+3p_3+4p_4.
\]
At an ordinary transition,
\[
 |B_i\cap B_{i+1}|=|B_i|+|B_{i+1}|-5,
\]
while at the seam the subtracted union rank is \(\rho\).  The two endpoint
vertices have ranks at most \(|B_1|\) and \(|B_p|\).  Summing all vertex
bounds gives
\[
 \sum_{i=0}^{p}|V_i|
   \le2R_{\rm pair}-5p+10-\rho,                  \tag{3.11}
\]
which is (6.1e).

If
\[
 L_{\rm lit}=z_1+2z_2+3z_3+4z_4,
\]
then the total rank of all masks of ranks one through four is \(1936\), so
\[
 R_{\rm pair}=1936-L_{\rm lit}-\rho.
\]
There are exactly \(y_1\) core vertices outside the middle segment, each of
rank at most four.  Thus
\[
 S\le3882+4y_1-5p-2L_{\rm lit}-3\rho,            \tag{3.12}
\]
confirming (6.1f).  Combining this with (5.7) gives
\[
 15p+6L_{\rm lit}+E+8\rho\le9708+7y_1.
\]
Substitution of the zero-margin formulas for \(p\) and \(y_1\) gives
\[
 29n_5+22\Delta_{\rm lit}
   +6L_{\rm lit}+E+8\rho\le10866,                \tag{3.13}
\]
so the constants in (6.1g) also pass.

## 4. The top chain-A slices

### 4.1 Elimination at \(n_5=134\)

Here
\[
 T=135-n_5-x_4=1-x_4\le1.
\]
Every zero-margin word has a carrier of rank three or four, but (3.3)
requires \(t_\ast\ge3\) or \(t_\ast\ge2\).  This is already a contradiction.
Thus \(D=0\) is impossible at \(n_5=134\).

The source's independent one-unit Hall argument is also correct.  Exact
rank-four rigidity gives
\[
 C=P_4\Vert D_3\Vert Q_4,
\]
with all pairs of \(D_3\) distinct selected rank-four witnesses and every
rank-at-most-three target literal.  A putative low \(H\) wholly inside
\(D_3\) contains two distinct rank-four pair values, so its OR has rank at
least five.  A putative low \(H\) meeting \(P_4\) or \(Q_4\) contains a
literal rank-four entry; if its OR has rank at most four, it equals that
already literal value and supplies no new carrier.  Hence the effective
carrier is zero.  The no-carrier Hall row gives
\[
 y_2\ge94+134+\Delta_{\rm lit}
       =228+\Delta_{\rm lit},
\]
whereas \(D=0\) requires
\[
 y_2=227+\Delta_{\rm lit}.
\]
The contradiction is exactly one unit.

### 4.2 Double filtration at \(n_5=133\)

Now \(T=2-x_4\).  The carrier budget forces
\[
 x_4=0,\qquad s_3=1,\qquad \rho=4,\qquad t_\ast=2.
\]
Equation (3.5) becomes \(k=2-g\).  Since \(k\ge2\) and \(g\ge0\),
\[
 g=0,\qquad k=2.
\]
Equation (3.1) and the zero-margin definitions then give
\[
 \boxed{
 \Delta_{\rm lit}=103-n_4,\quad
 y_1=n_4,\quad
 y_2=329-n_4,\quad
 n_4\le103.}                                     \tag{4.1}
\]

Write
\[
 C=P_4\Vert D_3\Vert Q_4,\qquad
 m=|D_3|=332-n_4.
\]
The complete pair ledger is:

- \(D_3\) has \(m-1=331-n_4\) pairs.
- Exactly \(m-3=329-n_4\) of them are the selected nonliteral rank-four
  pair witnesses.
- The remaining two are the consecutive seam pairs under \(H\).
- Their ORs are distinct nonliteral masks of rank at most three.
- There are \(n_4\) physical pairs outside \(D_3\); equality in the outer
  pair ledger makes all of them the \(y_1=n_4\) selected rank-five pairs.

A pair outside \(D_3\) contains a literal rank-four entry.  If its OR has
rank at most four, it equals that literal value, so it cannot carry one of
the two missing nonliteral lower masks.  This rules out a hidden third
location for either seam color.

There are \(m-2\) triples in \(D_3\).  No one contains a selected rank-five
pair.  The exact outer triple partition therefore makes one of them \(H\)
and all remaining
\[
 (m-2)-1=m-3=329-n_4=y_2
\]
distinct selected rank-five triple witnesses.  Their values are distinct
because the selected family contains one witness for each distinct
rank-five target.

The two seam colors are the only nonliteral masks below rank four.  Hence
\[
 (z_1,z_2,z_3)=
 \begin{cases}
 (11,54,164),&\text{seam ranks }(2,3)\text{ or }(3,2),\\
 (11,55,163),&\text{seam ranks }(3,3).
 \end{cases}                                      \tag{4.2}
\]
In both cases \(z_1+z_2+z_3=229\), so \(D_3\) has exactly
\[
 m-229=103-n_4
\]
repeated lower entries.

There is no artificial-concatenation issue here: \(D_3\) is an actual
segment of the original word.  Lemma 2.1 applies directly and gives:

> Every four-window of \(D_3\) is a selected witness for a distinct
> rank-six target.

This verifies (6.3).

Let \(s_0\) be the sum of the two seam-pair ranks.  Then \(s_0=5\) in the
\((2,3)\) case and \(s_0=6\) in the \((3,3)\) case.  The exact ledgers give
\[
\begin{aligned}
 U_2&=4(m-3)+s_0,\\
 U_3&=5(m-3)+4=5m-11,\\
 U_4&=6(m-3).
\end{aligned}
\]
Lemma 2.2 gives
\[
 R^{(2)}=m+12-s_0,\qquad R^{(3)}=m+4,             \tag{4.3}
\]
and therefore
\[
 \#\{\text{exact length-two zero runs}\}=8-s_0.  \tag{4.4}
\]
This is three in seam type \((2,3)\) and two in seam type \((3,3)\).
Five-window rank at least seven gives \(R^{(4)}\ge m+1\), so there are at
most three exact length-three zero runs.  Equations (6.4)--(6.5) pass once
the restricted-run definition in Lemma 2.2 is inserted.

### 4.3 Exhaustiveness of the \(n_5=133\) seam forms

The seam colors are distinct, nonliteral, proper lower subsets of the
rank-four value \(\operatorname{OR}(H)\).  A rank pair \((2,2)\) cannot
have union rank four because the two pairs contain the nonempty middle
entry.  Thus the possible rank pairs are exactly
\[
 (2,3),\ (3,2),\ (3,3).
\]

For type \((2,3)\), after relabelling,
\[
 B_2=\{x,y\},\qquad B_3=\{y,c,d\}.
\]
Their intersection is \(\{y\}\), so the middle physical entry is
\(\{y\}\).  The left entry must contain \(x\), but cannot also contain
\(y\), since then the nonliteral seam mask \(B_2\) would occur literally.
The right entry must contain \(c,d\), but cannot also contain \(y\), for the
same reason.  Hence the three entries are
\[
 \{x\},\ \{y\},\ \{c,d\},
\]
or the physical reversal.

For type \((3,3)\), write
\[
 B_L=I\cup\{a\},\qquad B_R=I\cup\{b\},\qquad |I|=2.
\]
The middle entry is a nonempty \(Y\subseteq I\).  If \(|Y|=1\), the outer
entries are forced to be
\[
 (I\setminus Y)\cup\{a\},\qquad
 (I\setminus Y)\cup\{b\}.
\]
If \(Y=I\), the left entry is \(\{a\}\) or \(\{a,i\}\) for one
\(i\in I\), and independently the right entry is \(\{b\}\) or
\(\{b,j\}\) for one \(j\in I\).  Including all of \(I\) with \(a\) or
\(b\) would make a missing seam target literal and is forbidden.

These lists are exhaustive, and their three entries are distinct.  Thus
(6.6) passes.

## 5. The five \(n_5=132\) modes

At \(n_5=132\),
\[
 T=3-x_4,\qquad
 k=T-s_3+1-g,\qquad
 \Delta_{\rm lit}=106-s_3-g-n_4.                 \tag{5.1}
\]
Also
\[
 y_1=105-\Delta_{\rm lit},\qquad
 y_2=225+\Delta_{\rm lit}.                        \tag{5.2}
\]

The mode enumeration is exhaustive:

- \(x_4=2\) gives \(T=1\), which cannot contain either carrier.
- If \(x_4=1\), then \(T=2\), so
  \(\rho=4,t_\ast=2,s_3=1\).  The inequality \(k\ge2\) forces \(g=0\).
- If \(x_4=0,\rho=3\), then \(t_\ast=3\), all slack is central,
  \(s_3=1\), and \(k\ge3\) forces \(g=0\).
- If \(x_4=0,\rho=4,t_\ast=2\), the one remaining slack unit is one
  singleton satellite; hence \(s_3=2\), and \(k\ge2\) forces \(g=0\).
- If \(x_4=0,\rho=4,t_\ast=3\), all slack is central and \(s_3=1\).
  Here \(k=3-g\ge2\), so \(g\in\{0,1\}\).

Substitution into (5.1)--(5.2) gives exactly the source table:

| mode | \((x_4,s_3,\rho,t_\ast,g)\) | \(\Delta_{\rm lit}\) | \(y_1\) | \(y_2\) |
|---|---:|---:|---:|---:|
| A | \((1,1,4,2,0)\) | \(105-n_4\) | \(n_4\) | \(330-n_4\) |
| B | \((0,2,4,2,0)\) | \(104-n_4\) | \(n_4+1\) | \(329-n_4\) |
| C0 | \((0,1,4,3,0)\) | \(105-n_4\) | \(n_4\) | \(330-n_4\) |
| C1 | \((0,1,4,3,1)\) | \(104-n_4\) | \(n_4+1\) | \(329-n_4\) |
| D | \((0,1,3,3,0)\) | \(105-n_4\) | \(n_4\) | \(330-n_4\) |

The following necessary ranges are omitted in the source:
\[
\begin{array}{c|c}
\text{mode}&\text{necessary range information}\\ \hline
A&2\le n_4\le104,\\
B&1\le n_4\le104,\\
C1&n_4\le104,\\
C0,D&n_4\le105.
\end{array}                                      \tag{5.3}
\]
The upper bounds come from \(\Delta_3\ge0\).  Mode A has \(x_4=1\), so
there must be at least two literal rank-four occurrences to have one
repetition.  Mode B has two lower components in one physical core, so at
least one rank-four position must separate them.  No positive lower bound
for \(n_4\) follows from this coarse ledger in C0, C1, or D.

Let \(M_3\) be the middle lower-pair vertex segment.  Its stated lengths
check:

- in A, C0, and D, \(M_3\) is the full lower component and has length
  \(333-n_4\);
- in B, it is the central component of length \(332-n_4\), with one
  isolated literal lower component outside;
- in C1, it has length \(332-n_4\), and one further low vertex is attached
  at an end through the unique embedded rank-five pair.

In every mode, every triple of \(M_3\) except \(H\) is a distinct selected
rank-five witness.  Lemma 2.1 then makes every four-window of \(M_3\) a
distinct selected rank-six witness.

Modes A, B, and C1 have exactly the two seam colors as their nonliteral
masks below rank four.  C0 has those two plus its one extra lower pair
color.  In D the two seam colors have rank two and \(H\) has rank three, so
\[
 (z_1,z_2,z_3)=(11,53,164).
\]
The same proper-subset argument used above forces the three seam entries in
D to be three distinct singletons.

Thus the five rows are complete as a list of coarse modes and cell-family
topologies.  They are not complete labelled realizations: the rows do not
decide all seam orientations, literal placements, the C0 extra-pair
location, the C1 tail side, or global OR compatibility, and they do not
prove existence for every admissible integer row.

## 6. Chain-B zero-margin analogues

The unmodified chain-B orientation, physical schedule, and coordinate
ledgers (7.1)--(7.6a) retain the PASS verdict of the preceding audit.  The
fresh checks here concern the newly added zero-margin path, recursive form,
top-slice seam argument, and deeper window identities.

Assume the duplicate-free chain-B schedule and
\[
 D_2=y_2-(95+n_5+\Delta_{\rm lit})=0.
\]
There is no low triple carrier.  The non-rank-five pairs form one actual
contiguous segment in the slack-two component \(C_2\), with
\[
 p=96+n_5+\Delta_{\rm lit},\qquad
 L=p+1,\qquad p-1=y_2.                            \tag{6.1}
\]
Every transition of its edge-color path is a distinct selected rank-five
triple.  Thus ordinary consecutive color ranks \(r,s\) obey \(r+s\ge6\).
Rank-two colors are separated by rank-four colors on this single path, so
\[
 p_2\le p_4+1.                                    \tag{6.2}
\]

Every cell of length at most three in the segment has rank at most five.
Lemma 2.1 gives
\[
 x_3\ge L-3=y_2-1,                                \tag{6.3}
\]
again after defining \(x_3\) locally.

The window sums are
\[
 U_2=R_{\rm pair},\qquad
 U_3=5(L-2),\qquad
 U_4=6(L-3).
\]
Lemma 2.2 gives
\[
\begin{aligned}
 R^{(2)}&=5L+1-R_{\rm pair},\\
 R^{(3)}&=L+3,\\
 \#\{\text{exact length-two zero runs}\}
   &=4L-2-R_{\rm pair}.
\end{aligned}                                    \tag{6.4}
\]
Five-window rank at least seven gives \(R^{(4)}\ge L+1\), hence at most two
exact length-three zero runs.  This verifies (7.6b)--(7.6d).

### 6.1 Chain-B recursive normal form

The two original lower components have only \(N-2\) physical internal
pairs.  The number not internal to one of the \(s_3\) rank-at-most-three
components is therefore
\[
 (N-2)-[(N-n_4)-s_3]=n_4+s_3-2.
\]
Consequently
\[
\begin{aligned}
 g
  &:=y_1-(n_4+s_3-2)\\
  &=369-2n_5-s_3-x_4-\Delta_3-n_4
  \ge0.                                           \tag{6.5}
\end{aligned}
\]
The one-unit shift relative to chain A is correct.

With \(T=135-n_5-x_4\), central slack \(t_\ast\), and
\[
 g_{\rm sat}=T-t_\ast-(s_3-1),\qquad
 g_c=g-g_{\rm sat},
\]
there is no carrier mask, so the nonliteral lower masks are exactly the
central pair cells not selected at ranks four or five:
\[
 k=t_\ast-1-g_c=T-s_3-g,\qquad
 z_1+z_2+z_3=231-k.                               \tag{6.6}
\]
Thus (7.6e)--(7.6f) is correct.  The same feasibility conditions
\[
 T-t_\ast\ge s_3-1,\qquad
 g_{\rm sat}\ge0,\qquad
 g\ge g_{\rm sat},\qquad g_c\ge0
\]
should be included when the equations are presented as a formal normal
form.

Chain C requires no separate calculation: it is the physical reversal of
chain B, and all counts above are reversal-invariant.

## 7. Chain-B top slice and the artificial seam

At \(n_5=134\), delete the intervening literal rank-five block and form
\[
 C^\ast=C_2\Vert C_1.
\]
All previously selected lower witnesses remain actual intervals wholly
inside \(C_2\) or \(C_1\).  Exact rank-four boundary--core rigidity gives
\[
 C^\ast=P_4\Vert D_3\Vert Q_4,\qquad
 |D_3|=331-n_4\ge231.                             \tag{7.1}
\]

The source's conclusion that the artificial concatenation seam does not
lie in \(D_3\) is correct, but its path-antichain mechanism is worth making
explicit.

Put \(m=|D_3|\).  There are \(m-1\) selected nonliteral rank-four witnesses
inside \(D_3\), each of length two or three.  Indeed, a nonliteral
rank-four witness cannot meet \(P_4\) or \(Q_4\): if it contains a literal
rank-four entry and still has rank four, its OR equals that literal value.
Suppose \(b>0\) of the \(m-1\) nonliteral witnesses are triples.  Then
\(m-1-b\) pair cells are selected, so exactly \(b\) of the \(m-1\) pair
positions are unselected.  Every selected triple contains two consecutive
pair positions, both of which must be unselected because the selected
same-rank intervals form an antichain.  Thus the \(b\) selected triples give
\(b\) distinct edges in the path graph induced by the \(b\) unselected pair
positions.  An induced subgraph of a path on \(b>0\) vertices has at most
\(b-1\) edges, a contradiction.  Hence \(b=0\): every pair of \(D_3\) is
one of the original selected rank-four witnesses.

If the artificial seam were inside \(D_3\), one of those required pairs
would be a nonexistent cross-component witness.  Therefore the seam lies
outside \(D_3\), and \(D_3\) is an actual physical segment of one original
component.  It cannot lie in \(C_1\), because every physical adjacent pair
of \(C_1\) is selected at rank five, while every adjacent pair of \(D_3\)
has rank four.  Consequently
\[
 D_3\subseteq C_2.                                \tag{7.2}
\]
This repairs every possible artificial-concatenation concern before
rank-six saturation is applied.

It follows that \(C_2\) is coordinate-complete and every entry of \(C_1\)
is a distinct literal rank-four entry.  To avoid the source's reuse of
\(m\), put \(\ell=|C_1|\).  Then
\[
 1\le\ell\le n_4\le100.
\]
There are \(329\) original internal pairs across \(C_2,C_1\), of which
\(330-n_4\) are the rank-four pairs in \(D_3\).  Pair-cell disjointness and
the fact that all \(\ell-1\) pairs of \(C_1\) are selected at rank five
give
\[
 \ell-1\le y_1\le n_4-1\le99.                    \tag{7.3}
\]
The other exact top-slice rows are
\[
 F=100-n_4,\qquad
 y_2\ge329-n_4,\qquad
 y_1+y_2=328.                                    \tag{7.4}
\]
All constants in (7.7)--(7.10) pass.

Now put \(m=|D_3|=331-n_4\).  Its \(m-1\) pairs are distinct selected
rank-four witnesses.  Chain B has no lower triple, so its \(m-2\) triples
are distinct selected rank-five witnesses.  Since \(D_3\subseteq C_2\) is
an actual segment, Lemma 2.1 makes all its \(m-3\) four-windows distinct
selected rank-six witnesses.

Therefore
\[
 U_2=4(m-1),\qquad U_3=5(m-2),\qquad U_4=6(m-3),
\]
and Lemma 2.2 gives
\[
 R^{(2)}=m+5,\qquad R^{(3)}=m+3.                 \tag{7.5}
\]
There are exactly two exact length-two zero runs.  The five-window argument
gives \(R^{(4)}\ge m+1\), so there are at most two exact length-three zero
runs.  Equation (7.10a) is correct.

## 8. General chain-B rows (7.11)--(7.14)

For every hypothetical chain-B word, the following forward implications are
correct:
\[
 0\le x_4\le134-n_5,\qquad
 1\le s_3\le135-n_5-x_4,                         \tag{8.1}
\]
\[
 \Delta_3+n_4
   \le369-2n_5-s_3-x_4,                          \tag{8.2}
\]
\[
 y_1\le133-n_5+z_4,                              \tag{8.3}
\]
and, for every coordinate set \(B\),
\[
 2Z_{B,3}-R_{B,3}-a_{B,4}\ge L_3(|B|).           \tag{8.4}
\]
The constants \(369\) and \(133\) correctly reflect the \(N-2\) physical
pair cells of two original low components.

At \(n_5=134\), (8.1) forces \(x_4=0,s_3=1\), and (8.3) gives
\(y_1\le n_4-1\).  But (8.2) gives only
\[
 \Delta_3+n_4\le100.                             \tag{8.5}
\]
The equality
\[
 \Delta_3+n_4=100
\]
comes from the stronger Section 7.1 boundary--core statement: \(D_3\) has
\(331-n_4\) positions and contains all \(231\) lower masks literally, so
its repetition excess is
\[
 \Delta_3=(331-n_4)-231=100-n_4.
\]
The patched source now makes exactly this distinction: it states the
inequality as the consequence of (7.11)--(7.14), and cites Section 7.1 for
the equality.  The revised paragraph is logically correct.

For smaller \(n_5\), (7.11)--(7.14) are exact only in this sense: every word
produces data satisfying them, with no loss in deriving the data.  They are
not an if-and-only-if numerical characterization.

The pointwise rows (5.39) and (7.14) are valid for every \(B\).  Their
displayed summed binomial moments must be restricted to
\[
 0\le t\le10.
\]
At \(t=11\), the left side is zero while the unsubtracted \(+1\) run term on
the displayed right side is positive.  This is a domain correction to
(5.40) and to the corresponding summed chain-B moment, not a defect in the
pointwise inequalities.

## 9. Required corrections, qualifications, and applied repair

The following list separates outstanding corrections from the Section 7.2
repair already applied during this audit.

1. Define \(x_3\) before (6.1b6) as the number of selected rank-six
   witnesses of physical length four.  Use the same definition in (7.6c).
2. In (6.4) and every subsequent zero-run formula, define zero runs in the
   coordinate traces restricted to the stated physical segment, including
   boundary-truncated runs and an all-zero trace as one full run.
3. Add the feasibility inequalities (3.6), and their carrier-free chain-B
   analogues, to the recursive normal forms.
4. Add the necessary \(n_4\)-ranges (5.3) to the five \(n_5=132\) modes.
5. No further change is required at the patched Section 7.2 passage.  It
   now correctly says that (7.11)--(7.14) give
   \(\Delta_3+n_4\le100\), and that equality uses the Section 7.1
   boundary--core argument.
6. Restrict (5.40), and the analogous summed moment following (7.14), to
   \(0\le t\le10\).
7. Qualify “completely classified” for \(n_5=132\) as “the coarse
   \((x_4,s_3,\rho,t_\ast,g)\) modes and induced cell-family topologies are
   exhaustive.”  Do not read it as labelled realizability or existence.
8. Likewise, (5.35)--(5.40) and (7.11)--(7.14) are lossless necessary
   word-to-data parameterizations, not sufficient scalar classifications.
9. Expand Section 2's input list to include named-cell shortening, the
   rank-four surplus-component theorem, exact boundary--core rigidity, and
   the coordinate-transversal theorem.
10. Rename one of the two unrelated variables \(m\) in Section 7.1:
    first it denotes \(|C_1|\), later \(|D_3|\).  The proof above uses
    \(\ell=|C_1|\) and \(m=|D_3|\).
11. Fix the following delimiter typographical errors:
    - after \(R^{(4)}\ge L+1\) near (6.1b7), delete the extra closing
      parenthesis;
    - replace “\(p+1)\)-vertex” by “\((p+1)\)-vertex” after (6.1k);
    - replace “\(C_2)\)” by “\(C_2\)” before (7.6b);
    - replace “\(L)\)-vertex” by “\(L\)-vertex” after (7.6f).

Items 1--4 and 6--11 are definition, scope, domain, or presentation
corrections.  Item 5 records a live repair already made while this audit was
being completed.  The earlier attribution error is absent from the current
text.

## 10. Adversarial audit

The strongest claims were tested against the following possible failure
modes.

### 10.1 Endpoint double charging

An outside rank-six interval may cross both endpoints of the test segment.
The proof charges it first by its left endpoint if that endpoint lies
before the segment, and only otherwise by its right endpoint.  The two
classes are disjoint.  Distinct left and right endpoints separately bound
their sizes, so no interval or endpoint is double-counted.

### 10.2 Same-rank containment or repeated target values

If one selected interval contains another, their OR masks are nested.
Equal cardinality forces equality, contrary to selecting distinct targets.
This proves the antichain property and also rules out a selected pair under
a selected triple of the same rank.  All “distinct witness” conclusions in
the pair, triple, and four-window ledgers are therefore justified either by
this antichain fact or by membership in a globally selected target family.

### 10.3 Artificial concatenation

The chain-B top-slice proof does not silently use the artificial seam as a
witness.  The induced-path argument in Section 7 proves first that all
rank-four witnesses in \(D_3\) are original pair cells.  That excludes the
seam from \(D_3\), after which \(D_3\subseteq C_2\) is a genuine physical
segment.  Only then are the triple and rank-six saturation arguments
applied.

### 10.4 Seam witness collisions

At \(n_5=133\), the two seam pair values are exactly the two pair cells left
after the \(m-3\) rank-four pair witnesses are placed.  Outer zero-margin
equality maps these cells injectively to the two missing lower masks.
They cannot coincide with one another, with a literal entry, or with
\(\operatorname{OR}(H)\).  The local forms in Section 4.3 respect all of
these exclusions.

### 10.5 Zero-run boundary leakage

The window identity was rederived for a segment-restricted trace.  It
counts a run truncated at either segment endpoint and counts an absent
coordinate once.  With this convention every displayed zero-run constant
checks.  With global runs the formulas can fail, so the missing definition
is mathematically material even though the intended calculations are
correct.

### 10.6 Missing \(n_5=132\) mode

The audit split first by \(x_4\), then by carrier rank, then by the only
possible values of \(t_\ast\).  The total slack is three, and every
satellite consumes at least one unit.  These alternatives leave precisely
A, B, C0, C1, and D.  No sixth coarse tuple is compatible with the carrier
and \(k\)-bounds.

### 10.7 Hidden converse

The normal forms preserve every hypothetical word, but their numerical
rows do not impose all label compatibility, interval order, coordinate
pins, or upper-rank coverage conditions.  Treating them as sufficient would
be an invalid inference.  The source usually warns that no bit assignment
is asserted; the few stronger phrases listed in Section 9 should be aligned
with that warning.

### 10.8 Top chain-B equality

Substitution into (7.11)--(7.14), without importing Section 7.1, yields only
(8.5).  The current source says exactly that.  It then invokes the exact
boundary--core fact that all \(231\) lower masks occur literally in \(D_3\),
which restores equality immediately and noncircularly.  The patched
argument passes.

## 11. Final theorem ledger

Conditional on the previously audited structural inputs, the following new
claims are verified:

- zero margin is impossible in chain A at \(n_5=134\);
- chain A at \(n_5=133\) has the exact double-filtration skeleton
  (4.1)--(4.4) and precisely the seam forms listed in Section 4.3;
- chain A at \(n_5=132\) has exactly the five coarse modes in Section 5;
- every claimed middle four-window is a distinct rank-six witness;
- all chain-A and chain-B zero-run identities are exact under the restricted
  trace convention;
- the recursive normal forms (3.1)--(3.5) and (6.5)--(6.6) are exact
  necessary word-to-data forms;
- the artificial-concatenation seam is rigorously excluded from the
  top chain-B \(D_3\), and \(D_3\subseteq C_2\);
- chain C follows by reversal.

No substantive algebraic error, witness-collision error, endpoint-counting
error, seam artifact, or omitted coarse \(n_5=132\) mode was found.  The
former Section 7.2 attribution error has been repaired.  The remaining
logical qualification is to avoid a converse overreading of the word
“classification.”
