# A/H synthesis: proportional-collar completion and row-coherent literal extraction

Date: 2026-07-25

Method: pure mathematics only. No finite search, solver, script, or web
input is used.

## 0. Verdict

Put

\[
 n=2m+1,\qquad W=\binom nm,\qquad B=W/n,\qquad
 H=\lceil A\sqrt m\rceil
\]

for fixed \(A>0\).  This note proves two exact composition theorems.

1. A selected family \(J\) of actual pointed cyclic flags extends to one
   integral balanced nested flag resolution whenever its crossings satisfy
   one explicit proportional-collar inequality at every adjacent-rank cut.
   There is no further divisibility, common-owner, or concatenation
   condition.

2. The audited pointed-extraction graph may be made **row coherent**.  If
   its retained incidence is \(\Omega(HW)\), then all \(\delta W\) desired
   distinct shoulder incidences can be placed on starts belonging to only

   \[
   O(B/H)
   \]

   whole wreath rows.  Emitting those complete literal row blocks costs

   \[
   O(W/H+B)=o(W)
   \]

   letters.  Thus an \(O(W)\) endpoint-sharing shoulder ledger can be
   appended to an existing U7/macro-packet word at sublinear cost.

The same argument does **not certify** the complete complement of the
advertised U7 shoulder support at linear local depth.  In one equal
four-box \(Q_R=[0,R]^4\), that certified-support complement through
\(h=\alpha R\) depths has

\[
 \left(\frac{\alpha^2}{2}-\frac{\alpha^3}{3}
       +\frac{\alpha^4}{24}+o(1)\right)R^4
 =\Theta(RM_R)
\]

distinct targets, where \(M_R=w(Q_R)=\Theta(R^3)\).  The row-coherent
appendage above explicitly supplies only \(O(M_R)\) flag incidences.  Thus
it is a factor \(R\) short of a designated witness for every target in that
certified complement.

This is not an unconditional hole lower bound: the U7 audit does not prove
that every target outside the certified support is absent from all
unadvertised U7 intervals or from cross-box intervals.  If a constant
fraction are genuine holes, endpoint throughput forces
\(\Omega(M_R)\) extra letters.  Otherwise the missing work is to prove and
exploit that incidental support.  The abstract balanced completion in the
first theorem is not a word and supplies neither alternative.

## 1. Exact proportional-collar completion

Let \(V_q=\binom{[n]}{m-q}\), \(N_q=|V_q|\), and

\[
 \lambda_q=\frac W{N_q},\qquad c_q=\lfloor\lambda_q\rfloor
 \qquad(0\le q\le H).
\]

Fix one oriented exact wreath factor \(F\).  Every pointed start
\(X\in V_0\) has its actual same-start cyclic flag

\[
 \Gamma_0(X)\supset\Gamma_1(X)\supset\cdots\supset\Gamma_H(X).
\]

Let \(J\subseteq V_0\) be a selected family of starts, and put

\[
 f_q(S)=|\{X\in J:\Gamma_q(X)=S\}|.
\tag{1.1}
\]

Assume

\[
 \boxed{f_q(S)\le c_q\qquad(q\le H,\ S\in V_q).}
\tag{1.2}
\]

For \(\mathcal A\subseteq V_q\), let

\[
 N_q(\mathcal A)
 =\{R\in V_{q-1}:S\subset R\text{ for some }S\in\mathcal A\}
\tag{1.3}
\]

and define the selected crossing count

\[
 C_q^J(\mathcal A)
 =|\{X\in J:
       \Gamma_{q-1}(X)\in N_q(\mathcal A),\
       \Gamma_q(X)\notin\mathcal A\}|.
\tag{1.4}
\]

Define also the exact proportional collar

\[
 \Lambda_q(\mathcal A)
 =\lambda_{q-1}|N_q(\mathcal A)|
  -\lambda_q|\mathcal A|.
\tag{1.5}
\]

The normalized matching property of consecutive Boolean ranks gives
\(\Lambda_q(\mathcal A)\ge0\).

### Theorem 1.1 — a selected cyclic core has an integral balanced completion

If

\[
 \boxed{
 C_q^J(\mathcal A)\le\Lambda_q(\mathcal A)
 \quad
 (1\le q\le H,\ \mathcal A\subseteq V_q),
 }
\tag{PC}
\]

then there is one integral nested resolution

\[
 P_0(X)\supset P_1(X)\supset\cdots\supset P_H(X)
 \qquad(X\in V_0)
\]

such that

\[
 P_q(X)=\Gamma_q(X)\qquad(X\in J,\ q\le H)
\tag{1.6}
\]

and every depth-\(q\) target has load \(c_q\) or \(c_q+1\).

#### Proof

At transition \(q\), prescribe residual parent supplies and child demands

\[
 u_{q-1}(R)=\lambda_{q-1}-f_{q-1}(R),
 \qquad
 v_q(S)=\lambda_q-f_q(S).
\tag{1.7}
\]

They are nonnegative by (1.2), and both have total mass \(W-|J|\).
For every child family \(\mathcal A\), the fractional transportation Hall
inequality is

\[
 v_q(\mathcal A)\le u_{q-1}(N_q(\mathcal A)).
\tag{1.8}
\]

Every selected child in \(\mathcal A\) has its selected parent in
\(N_q(\mathcal A)\).  Hence

\[
 f_{q-1}(N_q(\mathcal A))-f_q(\mathcal A)
 =C_q^J(\mathcal A).
\tag{1.9}
\]

Substituting (1.7) into (1.8) and using (1.9) shows that (1.8) is exactly
\((\mathrm{PC})\).  Thus a nonnegative fractional residual flow exists
between every adjacent pair of ranks.  Its parent and child throughputs
agree at every intermediate node, so the adjacent flows concatenate into
one fractional residual flow through the whole layered inclusion network.

Now impose the integral node-throughput bounds

\[
 c_q-f_q(S)
 \le h_q(S)\le
 c_q+1-f_q(S)
\tag{1.10}
\]

on the residual flow.  At depth zero impose the exact value
\(h_0(X)=1-\mathbf1_J(X)\).  The fractional flow just constructed has
node throughput \(\lambda_q-f_q(S)\), which lies in (1.10).  All lower and
upper bounds are integral.  After the standard lower-bound reduction, the
constraint matrix is a directed incidence matrix; network integrality
therefore supplies an integral residual flow.

Decompose it into \(W-|J|\) integral paths and add the \(|J|\) prescribed
cyclic paths.  The total load at \(S\) lies in
\(\{c_q,c_q+1\}\), and every middle root occurs once.  This proves
(1.6) and the balanced conclusion. \(\square\)

### Complement form and automatic cuts

Put

\[
 \mathcal B=V_q\setminus\mathcal A,\qquad
 \mathcal P=V_{q-1}\setminus N_q(\mathcal A).
\]

Thus every child of a parent in \(\mathcal P\) lies in \(\mathcal B\).
Since the total selected and proportional masses agree at the two ends,
\((\mathrm{PC})\) is equivalently

\[
 \boxed{
 f_q(\mathcal B)-f_{q-1}(\mathcal P)
 \le
 \lambda_q|\mathcal B|-\lambda_{q-1}|\mathcal P|.
 }
\tag{1.11}
\]

The left side is the number of selected edges entering \(\mathcal B\)
from outside \(\mathcal P\); the right side is the uniform fractional
flow across the same directed boundary.

Two useful classes are automatic.

* If \(\Lambda_q(\mathcal A)\ge |J|\), then (PC) holds because
  \(C_q^J(\mathcal A)\le|J|\).
* If \(\mathcal P=\varnothing\), then
  \[
  f_q(\mathcal B)\le c_q|\mathcal B|
  \le\lambda_q|\mathcal B|,
  \]
  so (1.11) holds.

Consequently only near-tight Boolean-shadow cuts with a nonempty
full-parent core can obstruct a selected cyclic core.  This is the explicit
integral inequality left by the A/H composition.

## 2. Row-coherent extraction from the audited incidence graph

Use the literal wreath block

\[
 E_0,E_1,\ldots,E_{n-1},E_0,E_1,\ldots,E_{2H},
\qquad E_j=I_\pi(j,m-H).
\tag{2.1}
\]

It has \(n+2H+1\) nonzero letters and physically exposes the complete
signed depth-\(H\) flag at each of its \(n\) original starts.

Assume the audited cap-and-parent-pruning theorem has produced a bipartite
graph \(G\) with:

* the \(W\) pointed starts on the left, grouped into \(B=W/n\) wreath rows;
* prescribed signed shoulder targets on the right;
* left degree at most \(d\le2H+2\);
* right degree at most a fixed \(\Delta=\Delta_A\);
* at most one edge in each start--product-parent cell; and
* for some fixed \(\varepsilon>0\),
  \[
  e(G)\ge\varepsilon HW.
  \tag{2.2}
  \]

### Theorem 2.1 — whole-row pointed extraction

For every fixed \(\delta>0\), there is a constant
\(C=C(A,\varepsilon,\delta)\) and a set of at most

\[
 r=\left\lceil\frac{CB}{H}\right\rceil
\tag{2.3}
\]

whole wreath rows whose literal blocks contain
\(D=\lfloor\delta W\rfloor\) globally distinct prescribed targets.  The
targets assigned to one start belong to distinct product parents, and
their same-left-endpoint sharing excess is

\[
 D-O(W/H)=\delta W-O(W/H).
\tag{2.4}
\]

The total emitted length of those complete row blocks is

\[
 \boxed{
 r(n+2H+1)
 =O_{A,\varepsilon,\delta}(W/H+B+n)
 =o(W).
 }
\tag{2.5}
\]

#### Proof

Take

\[
 s=\left\lfloor\frac{\varepsilon H}{4}\right\rfloor.
\]

For large \(m\), \(1\le s\le d\).  Let \(M_s\) be the number of starts
of degree at least \(s\).  Since every other start has degree at most
\(s-1\), while every start has degree at most \(d\),

\[
 e(G)\le(s-1)W+(d-s+1)M_s.
\]

Using (2.2), \(d\le2H+2\), and large \(H\), we obtain

\[
 M_s\ge\eta W
\tag{2.6}
\]

for a constant \(\eta=\eta(\varepsilon)>0\).

Let \(h_i\) be the number of these high-degree starts in row \(i\), and
order the rows so that \(h_1\ge h_2\ge\cdots\ge h_B\).  The average of
the first \(r\) terms is at least the average of all \(B\) terms.  Hence

\[
 \sum_{i=1}^r h_i
 \ge\frac rB M_s
 \ge\eta nr.
\tag{2.7}
\]

Call the high starts in these rows \(J_0\).  Every subset
\(X\subseteq J_0\) has

\[
 s|X|\le e(X,N(X))\le\Delta|N(X)|.
\]

Thus, with \(b_s=\lfloor s/\Delta\rfloor=\Theta(H)\),

\[
 |N(X)|\ge b_s|X|.
\tag{2.8}
\]

Clone every start \(b_s\) times.  Hall's theorem gives a
\(b_s\)-fold matching from \(J_0\) to globally distinct targets.
Equations (2.3) and (2.7) give

\[
 b_s|J_0|
 \ge(\Theta(H))\,\eta n\,\frac{CB}{H}
 =\Theta(CW).
\]

Choose \(C\) large enough that this is at least
\(D=\lfloor\delta W\rfloor\), and retain exactly \(D\) matched edges,
using

\[
 O(\delta W/b_s)=O(W/H)
\]

starts.  The start--parent pruning gives distinct parents at each start.
If \(d_x\) targets are retained at start \(x\), the sharing excess is

\[
 \sum_x(d_x-1)_+
 =D-\#\{x:d_x>0\}
 =\delta W-O(W/H).
\]

Finally, all used starts lie in the \(r\) chosen rows.  Emitting (2.1) for
those rows costs exactly \(r(n+2H+1)\).  Since \(B=W/n\),
\(H=\Theta(\sqrt m)\), and \(n=\Theta(m)\), this is

\[
 O(W/H)+O(B)+O(n)=o(W).
\]

Every matched edge is one of the literal same-start flag intervals in its
emitted block. \(\square\)

### Corollary 2.2 — literal appendage to a macro-packet word

Let \(\mathscr U\) be any existing literal U7/macro-packet word on the same
Boolean coordinates.  Concatenate the row blocks from Theorem 2.1 after
\(\mathscr U\).  Every old U7 witness remains internal to its old epoch,
and every new shoulder witness remains internal to its row block.  No seam
identity is required and no connector letter is charged.  Therefore the
new word has length

\[
 |\mathscr U|+O(W/H+B)=|\mathscr U|+o(W)
\tag{2.9}
\]

and supplies literal witnesses for the \(D\) distinct targets and the
sharing excess (2.4).  Some of those masks may already have incidental U7
witnesses; no novelty claim is needed.

The physical endpoint ledger is exact.  This splice reuses **zero** old
U7 positions: it preserves every old witness and adds
\(r(n+2H+1)\) new positions.  Among the \(rn\) original
(non-prefix-copy) starts in the appended rows, only

\[
 p=O(W/H)
\]

are designated portals.  They own \(D=\lfloor\delta W\rfloor\) selected target
incidences, so their new-position same-left-endpoint reuse is exactly
\(D-p=\delta W-O(W/H)\).  The other new positions and duplicated row
prefixes are overhead already included in (2.5).  Thus (2.9) is an
appendage theorem, not a claim that a cyclic portal has been identified
with an existing U7 endpoint.

The appended rows should likewise not be counted as new middle-owning
macro-packets: their middle masks duplicate masks already owned by
\(\mathscr U\).  They are a sublinear repair epoch.  This is harmless for
the literal word-length theorem, but it does not improve the U7
middle-owner/state-surplus ledger by reassignment.

If one insists on the ordered-state/MTF interpretation, prepend the
complement of the first letter only once to the concatenated raw word.
The contiguous-OR statement itself requires no initialization letter.

The selected starts and all their advertised flags are physical.  The
balanced resolution supplied by Theorem 1.1, when (PC) also holds, is only
an integral completion certificate; none of its unselected abstract flags
is emitted or used in (2.9).

There is no hidden implication from Theorem 2.1 to (PC).  The matching in
Theorem 2.1 makes only the **assigned** signed targets globally distinct.
Two selected rows may still repeat an unassigned depth-\(q\) cyclic target,
so their full load \(f_q\) may exceed \(c_q\), especially on the
\(c_q=1\) plateau.  It may also violate a near-tight crossing cut.  Thus
the physical \(o(W)\)-appendage theorem is unconditional under (2.2), but
the claim that the same whole-row core sits inside one balanced resolution
requires the additional hypotheses of Theorem 1.1.

### Corollary 2.3 — direct audited-spill form

In the notation of the audited pointed-extraction theorem, suppose

\[
 S_{\mathcal T}-\mathcal E_{\mathcal A}(F)
 \ge\varepsilon HW.
\tag{2.10}
\]

Its same-parent collision loss is \(o(W)\), so for large \(m\) the pruned
graph satisfies (2.2), with (say) \(\varepsilon/2\) in place of
\(\varepsilon\).  Therefore the \(\delta W\) endpoint-sharing ledger can
be appended to any literal U7/macro-packet word in

\[
 O_{A,\varepsilon,\delta}(W/H+B)=o(W)
\]

letters, using whole exact-factor wreath rows.  This is a literal
strengthening of start-level extraction: it pays for physically emitting
the selected starts when the ambient base word is not already the full
wreath word.

Because \(\delta>0\) is arbitrary but fixed, it may be chosen larger than
the fixed coefficient in the audited equal-shell endpoint-sharing toll
(after multiplying by the fixed positive-mass parent fraction).  Hence the
appendage has enough **numerical sharing capacity** to pay that toll.  This
remains a necessary-ledger statement: it does not imply that all targets
missing from the U7 support have acquired witnesses.

## 3. Why the appendage does not certify the full U7 support complement

For the equal four-box

\[
 Q_R=[0,R]^4,\qquad
 M_R=w(Q_R)=\frac{2R^3+6R^2+7R+3}{3},
\]

the audited U7 support complement through upper depth \(h\) is exactly

\[
 \mathcal D_R(h)
 =(R+1)\bigl((R+1)A_h-B_h\bigr)
  +\frac{A_h^2-A_h}{6},
\tag{3.1}
\]

where

\[
 A_h=\frac{h(h+1)}2,\qquad
 B_h=\frac{h(h+1)(2h+1)}6.
\]

If \(h=\alpha R+O(1)\), with fixed \(0<\alpha\le1\), then direct
substitution gives

\[
 \boxed{
 \mathcal D_R(h)
 =
 \left(
 \frac{\alpha^2}{2}
 -\frac{\alpha^3}{3}
 +\frac{\alpha^4}{24}
 +o(1)
 \right)R^4.
 }
\tag{3.2}
\]

The coefficient is positive on \(0<\alpha\le1\).  Hence

\[
 \mathcal D_R(h)=\Theta(RM_R).
\tag{3.3}
\]

One pointed cyclic start supplies at most one target at each rank, hence
at most \(O(h)=O(R)\) targets in this shoulder.  Thus a surface-size
appendage with \(O(M_R/R)\) starts can explicitly designate witnesses for
only \(O(M_R)\) of the \(\Theta(RM_R)\) targets in (3.3).  No local
wreath-row incidence model is asserted here; this is only the universal
per-start rank count.

If all targets in (3.3), or any fixed positive fraction of them, are
genuinely absent from the old ambient word, covering them by appended
cyclic flags requires \(\Omega(M_R)\) starts and hence cannot be an
\(o(M_R)\)-length repair.  The antecedent is not proved by the U7
certified-support ledger.

This is not merely a feature of the chosen row blocks.  If a word \(C\)
of length \(L\) is appended to any old word, every genuinely new target
has a witness ending at one of the \(L\) new right endpoints.  The suffix
ORs ending at one endpoint form a chain, so that endpoint represents at
most one target in each fixed rank.  Across \(O(R)\) shoulder ranks, the
appendage can therefore introduce at most \(O(RL)\) new targets, including
all seam-crossing witnesses.  Consequently, **if**
\(\Omega(RM_R)\) members of the certified complement are actual old-word
holes, then \(L=\Omega(M_R)\).

Likewise, on any positive-mass compact family of typical four-chain boxes,
\(R=\Theta(\sqrt k)\), the sum of their widths is \(\Theta(W(k))\), and
their certified linear-depth U7 support complements total
\(\Theta(\sqrt k\,W(k))\).  An \(o(W(k))\)-letter appendage has total
rankwise endpoint throughput only \(o(\sqrt k\,W(k))\).  Thus sparse
cyclic-row appendage cannot certify all those complements by new
endpoints.  It is not ruled out that unadvertised old or cross-box
intervals already cover a large portion.

The distinction is exact:

* the endpoint-dual/fusion ledger asks for \(O(M_R)\) strategically shared
  target incidences, and Theorem 2.1 can supply that many at \(o(M_R)\)
  append cost;
* the complete complement of the certified support has
  \(\Theta(RM_R)\) members at linear depth, and cannot all be supplied by
  the same sparse appendage; its actual-hole count is not established.

## 4. The physical remaining gate

The abstract balanced flag factor contains every band target, but a flow
decomposition is not a contiguous-OR word.  Theorem 1.1 only says that a
selected physical cyclic core can coexist with such a flow.

To cover the complete shoulder at coefficient one, the remaining
\(\Theta(RM_R)\) incidences must be realized on the existing
\(M_R+o(M_R)\) baseline positions.  Equivalently, one needs either:

1. a replacement of the U7 principal endpoints by balanced flag prefixes
   which preserves the U7 internal witnesses; or
2. an ordered-state path cover of the balanced flags with
   \(o(W/H)\) one-update runs, giving the already audited length
   \(W+2HJ+1=W+o(W)\).

This is precisely the balanced-flag rotor gate.  The proportional-collar
inequality (PC) removes an abstract integral-completion obstruction for a
selected core, but it does not produce the one-update chronology and does
not turn the remaining abstract flags into physical endpoints.

## 5. Exact remaining selection inequality

The strongest clean A/H selection target exposed here is:

> Select \(O(B/H)\) whole rows whose high-degree starts carry the desired
> \(O(W)\) prescribed endpoint incidences and whose full selected cyclic
> core \(J\) obeys \(f_q\le c_q\) and
> \[
> C_q^J(\mathcal A)
> \le
> \lambda_{q-1}|N_q(\mathcal A)|-\lambda_q|\mathcal A|
> \quad(q\le H,\ \mathcal A\subseteq V_q).
> \]

Theorem 1.1 would then extend that same literal core to an integral
balanced resolution, and Theorem 2.1 would emit the useful physical part
at \(o(W)\) cost.  This selection inequality is unproved.  Even if proved,
it absorbs the \(O(W)\) portal-sharing ledger, not the
\(\Theta(HW)\)-sized full missing shoulder; the latter still requires the
rotor/replacement gate in Section 4.
