# Promotion rings: the two-top moving-hole transfer and full-cube rigidity

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad 2\le H,\qquad 2H<M-1.
\tag{0.1}
\]

There is a literal two-top exchange of one-hole promotion frames which
preserves the complete retained middle-owner multiset and is nevertheless
non-load-neutral at every lower depth \(1\le q\le H\).  At depth \(q\)
its entire action is one unit transfer

\[
 \boxed{\Delta_q=e_{X_q}-e_{Y_q},\qquad
        |X_q|=|Y_q|=m-q,\qquad \|\Delta_q\|_2^2=2,}
\tag{0.2}
\]

where

\[
 X_{q+1}\subset X_q,\qquad Y_{q+1}\subset Y_q.
\tag{0.3}
\]

Thus the all-lower-depth squared action is exactly

\[
                         \sum_{q=1}^H\|\Delta_q\|_2^2=2H.
\tag{0.4}
\]

On the untagged upper trace rows the action is also explicit: it is a
difference of two disjoint unit transfers, of squared norm \(4\), for
every \(1\le q<H\), and is zero at the top endpoint \(q=H\). Hence the
complete two-sided untagged squared action is \(6H-4\).

For every collision energy, and hence for every floor-corrected energy
differing from it by a fixed linear baseline, the exact depth-\(q\)
change is

\[
 \boxed{\Phi_q(\lambda_q+\Delta_q)-\Phi_q(\lambda_q)
       =\lambda_q(X_q)-\lambda_q(Y_q)+1.}
\tag{0.5}
\]

Consequently this orientation is strictly decreasing precisely when the
removed target is at least two load units heavier than the added target.
For a nonnegative weighted all-depth energy the corresponding criterion
is the signed sum of (0.5). The move is therefore a genuine physical
one-frame-per-top balancing direction, not another load-neutral holonomy.
It does not by itself prove that every positive-energy state contains a
favorably charged copy. There is also an exact ownership caveat: each
isolated two-frame endpoint has \(H-1\) repeated middle owners, so the
primitive is not by itself an edge switch inside a squarefree one-hole
owner matching.

The construction uses the fact that the deleted phase is part of a
one-hole column and is allowed to move.  This is essential.  In the full
undeleted catalogue, or for a checkerboard cube trade between two
common-base patterns with no moving hole, there is an exact rigidity:

> If its aggregate middle action is zero, then its aggregate action is
> zero at every lower depth.

This holds in every cube dimension and for arbitrary permutations of the
core and placeholder positions. It includes the four-top and eight-top
common-base proposals, including mixed core--placeholder patterns. Thus
the smallest nonneutral primitive in the unrestricted one-frame-per-top
catalogue is not a six- or eight-top full cube: it is the moving-hole
two-top seam below. A squarefree owner-matching primitive still requires
a larger collar or circuit.

The exchange is in the unrestricted physical frame catalogue.  It lies
in a fixed mechanical support only when the two adjacent seam positions
have the same mechanical colour and the three seam labels have that shore
colour.  No claim of a uniformly dense mechanical subcatalogue is made.

## 1. Coherently punctured frame rows

Let \(U\) be an \(M\)-set with a directed cyclic frame \(\pi\).  For a
phase \(i\), the promotion trace of signed rank \(m+r\) has the form

\[
 C_{U,i}(r)=U\setminus Q_{\pi,i}(H-r),
\tag{1.1}
\]

where \(Q_{\pi,i}(h)\) is the cyclic \(h\)-interval with the terminal
endpoint prescribed by phase \(i\).  This is exactly the convention

\[
 C_{U,i}(r)=U\setminus
 \{c_{i+H+r},\ldots,c_{i+2H-1}\}.
\tag{1.2}
\]

A one-hole frame deletes one phase \(i_*\).  The same phase is absent
from every untagged trace row, so its omitted interval always has the same
terminal endpoint.  At the middle row \(r=0\), the retained owners are
the complements of all but one cyclic \(H\)-interval.

For the lower depth \(q\ge0\), put

\[
 h_q=H+q,\qquad r=-q.
\tag{1.3}
\]

The lower target is an \((m-q)\)-set, the complement in \(U\) of the
length-\(h_q\) interval with the phase's fixed terminal endpoint.

At \(q=0\) this direct set \(X=U\setminus Q\) is the middle owner. In
the root convention, with root \(A_U=[n]\setminus U\), the corresponding
middle target is

\[
                         D=A_U\cup Q=[n]\setminus X.
\tag{1.4}
\]

Global complementation is a bijection of the middle layer. Therefore
every middle-load identity below is literally equivalent in the direct
owner and root-target conventions. At \(q>0\) we state the action on the
direct lower targets \(U\setminus Q\).

## 2. The two-top seam

Let

\[
 C=\{z,y_0,y_1,\ldots,y_{L-2}\},\qquad L=M-1,
\tag{2.1}
\]

and choose two labels \(a_0,a_1\notin C\).  Put

\[
                         U_i=C\cup\{a_i\}\qquad(i=0,1).
\tag{2.2}
\]

On the abstract alphabet \(C\cup\{A\}\), take the two cyclic words

\[
\begin{aligned}
 \pi&=(A,z,y_0,y_1,\ldots,y_{L-2}),\\
 \rho&=(A,y_0,y_1,\ldots,y_{L-2},z).
\end{aligned}
\tag{2.3}
\]

They differ only by moving \(z\) across the cyclic seam at \(A\); after
a rotation this is an adjacent transposition of \(A\) and \(z\).  Let
\(\pi_i,\rho_i\) denote the specializations \(A\mapsto a_i\).

The core labels form one linear run between the two sides of \(A\).  In
\(\pi\), delete the phase whose middle omitted interval is the left end
window

\[
                         E_L=\{z,y_0,\ldots,y_{H-2}\}.
\tag{2.4}
\]

In \(\rho\), delete the phase whose middle omitted interval is the right
end window

\[
                         E_R=\{y_{L-H},\ldots,y_{L-2},z\}.
\tag{2.5}
\]

Call these punctured frames \(\pi_i^-\) and \(\rho_i^-\).  Consider the
two literal selections

\[
 \mathcal O=\{\pi_0^-,\rho_1^-\},\qquad
 \mathcal N=\{\rho_0^-,\pi_1^-\}.
\tag{2.6}
\]

Both selections use exactly one repaired frame at each of the same two
tops.

### Theorem 2.1 (exact moving-hole transfer)

The selections in (2.6) have identical retained middle-owner multisets.
At every lower depth \(1\le q\le H\), their load difference
\(\mathcal N-\mathcal O\) is

\[
 \Delta_q=e_{K_q\cup\{a_1\}}-e_{K_q\cup\{a_0\}},
\tag{2.7}
\]

where

\[
\begin{aligned}
 Q_q^*&=\{z,y_0,\ldots,y_{H+q-2}\},\\
 K_q&=C\setminus Q_q^*
     =\{y_{H+q-1},\ldots,y_{L-2}\}.
\end{aligned}
\tag{2.8}

In particular, \(|K_q|=m-q-1\), so the two sets in (2.7) have rank
\(m-q\), and

\[
 K_{q+1}=K_q\setminus\{y_{H+q-1}\}.
\tag{2.9}

#### Proof

First compare the two specializations of one fixed abstract word, say
\(\alpha\in\{\pi,\rho\}\).  If an omitted interval contains the
placeholder \(A\), then its complementary target is a subset of \(C\)
and is identical at \(U_0\) and \(U_1\).  It cancels in

\[
       L_q(\alpha_0^-)-L_q(\alpha_1^-).
\tag{2.10}
\]

If the omitted interval is a core-only set \(Q\subset C\), its two
complementary targets are

\[
                    (C\setminus Q)\cup\{a_0\},\qquad
                    (C\setminus Q)\cup\{a_1\}.
\tag{2.11}
\]

Thus (2.10) is the signed sum of (2.11) over the retained core-only
omitted intervals of \(\alpha\).

At length \(H\), the core-only intervals of \(\pi\), in their linear
order, consist of its exceptional left interval \(E_L\) followed by all
the internal intervals.  Those of \(\rho\) consist of the same internal
intervals followed by its exceptional right interval \(E_R\).  Deleting
\(E_L\) from \(\pi\) and \(E_R\) from \(\rho\) leaves exactly the same
family.  Equation (2.10), first for \(\rho\) and then for \(\pi\), now
shows

\[
 L_0(\rho_0^-)+L_0(\pi_1^-)
 =L_0(\pi_0^-)+L_0(\rho_1^-).
\tag{2.12}
\]

This is literal equality of the global middle-owner load vectors.

Now let \(h=H+q\), with \(q\ge1\).  The deleted phase of \(\pi\) has
terminal endpoint \(y_{H-2}\).  Its length-\(h\) omitted interval extends
past the left end of the core run and contains \(A\), so it removes no
core-only interval.  Hence all core-only length-\(h\) intervals of
\(\pi\) remain.  The deleted phase of \(\rho\) has terminal endpoint
\(z\); it removes the exceptional right length-\(h\) core interval.

Every nonexceptional core interval of \(\pi\) equals one of \(\rho\):
the interval of \(\pi\) beginning at \(y_j\) equals the interval of
\(\rho\) beginning at the same label.  After the two deletions, the only
unpaired core interval is therefore the exceptional left interval of
\(\pi\), namely

\[
                         Q_q^*=\{z,y_0,\ldots,y_{h-2}\}.
\tag{2.13}
\]

Using (2.10)--(2.11) in the difference

\[
 [L_q(\rho_0^-)-L_q(\rho_1^-)]
 -[L_q(\pi_0^-)-L_q(\pi_1^-)]
\tag{2.14}

gives exactly (2.7).  Equations (2.8)--(2.9) and
\(M-H=m\) give the stated ranks and nesting.  The two basis vectors in
(2.7) are distinct, proving \(\|\Delta_q\|_2^2=2\).  \(\square\)

### Corollary 2.2 (middle-load legality and the squarefree caveat)

Replacing \(\mathcal O\) by \(\mathcal N\) preserves the complete
retained middle load exactly. However, each of \(\mathcal O\) and
\(\mathcal N\) has exactly \(H-1\) internally repeated middle owners.
In particular, for \(H\ge2\), neither endpoint can occur inside a
squarefree one-hole owner matching.

#### Proof

The touched top markers are the same and (2.12) says that the entire
touched middle load vector is unchanged.

A common owner of \(\pi_0^-\) and \(\rho_1^-\) must be a subset of
\(U_0\cap U_1=C\). Its two omitted intervals therefore have the form

\[
                         R\cup\{a_0\},\qquad
                         R\cup\{a_1\},
\tag{2.13a}
\]

for the same \((H-1)\)-set \(R\subset C\). Equivalently,
\(R\cup\{A\}\) must be an \(H\)-window in both abstract words \(\pi\)
and \(\rho\). These words differ by transposing the adjacent symbols
\(A,z\). Their common \(H\)-windows containing \(A\) are exactly the
windows containing both \(A\) and \(z\), of which there are \(H-1\).
Indeed, according as there are \(k=0,\ldots,H-2\) symbols before \(A\)
in \(\pi\), the same set has \(k+1\) symbols before \(A\) in \(\rho\).
The two exceptional windows containing \(A\) but not \(z\) use opposite
ends of the core path and are distinct because \(2H<M\). The deleted
windows (2.4)--(2.5) do not contain \(A\), so none of these \(H-1\)
common owners is removed. The same argument, with the tops interchanged,
applies to \(\mathcal N\). \(\square\)

The result is stronger than a formal signed-array identity: all four
objects in (2.6) are actual one-hole cyclic frames. No fixed-top one-hole
rigidity is contradicted, because the load cancellation transfers owners
between the two adjacent tops. Corollary 2.2 is why an additional
squarefree collar is required before this algebraic primitive can be used
inside an owner matching.

### Proposition 2.3 (upper trace action)

For \(1\le q<H\), put \(h=H-q\) and

\[
\begin{aligned}
 Q^{\rm L}_q&=\{z,y_0,\ldots,y_{h-2}\},\\
 Q^{\rm D}_q&=\{y_{q-1},\ldots,y_{H-2}\},\\
 K^{\rm L}_q&=C\setminus Q^{\rm L}_q,
 \qquad K^{\rm D}_q=C\setminus Q^{\rm D}_q,\\
 \eta_K&=e_{K\cup\{a_0\}}-e_{K\cup\{a_1\}}.
\end{aligned}
\tag{2.15}
\]

At signed rank \(m+q\), the untagged retained-phase load change is

\[
 \boxed{\Delta_q^+=\eta_{K^{\rm D}_q}-\eta_{K^{\rm L}_q},
        \qquad \|\Delta_q^+\|_2^2=4.}
\tag{2.16}
\]

At \(q=H\) it is zero. Therefore the total two-sided squared action,
including (0.4), is

\[
                         2H+4(H-1)=6H-4.
\tag{2.17}
\]

#### Proof

The deleted phase of \(\pi\) has terminal endpoint \(y_{H-2}\). Its
length-\(h\) interval is \(Q^{\rm D}_q\), an internal core interval.
The deleted phase of \(\rho\), whose endpoint is \(z\), removes the
exceptional right core interval. Before deletion the two core decks
consist of the same internal intervals, together with the exceptional
left interval \(Q^{\rm L}_q\) for \(\pi\) and the exceptional right
interval for \(\rho\). Hence the retained core deck of \(\rho\) minus
that of \(\pi\) is

\[
                         Q^{\rm D}_q-Q^{\rm L}_q.
\]

The specialization cancellation (2.10)--(2.11) gives (2.16). The two
core sets in (2.15) are distinct because \(Q^{\rm L}_q\) contains \(z\)
and \(Q^{\rm D}_q\) does not. Thus the four displayed target basis
vectors are distinct, proving the norm. When \(q=H\), the omitted
interval is empty and every retained phase has target \(U_i\),
independently of the cyclic order and deleted phase; the two endpoint
loads agree. \(\square\)

Proposition 2.3 concerns the untagged row in which every retained phase
is counted. A preassigned nested tag schedule may suppress some of these
terms and is not claimed to be preserved; this is one of the remaining
gates in Section 5.

### Proposition 2.4 (two tops are minimal)

No one-top exchange of untagged one-hole frames can preserve its retained
middle-owner family and change an interval load at another rank. Hence
Theorem 2.1 has the smallest possible number of touched tops.

#### Proof

Complement the \(M-1\) retained middle owners inside the fixed top. They
are \(M-1\) cyclic \(H\)-intervals. Join two when their intersection has
size \(H-1\). Since \(2H<M\), this is the path obtained from the cyclic
start graph \(C_M\) by deleting the missing interval. Along the path,
successive set differences recover the cyclic labels, hence the missing
interval and the whole cyclic order, up to reversal and rotation. Those
dihedral ambiguities preserve every untagged interval deck. Thus a second
one-hole frame with the same retained middle family has exactly the same
load at every rank. \(\square\)

## 3. Exact floor action

Let \(\lambda_q(S)\) be the ambient integer load at rank \(m-q\) before
the switch, and orient (2.7) as

\[
                         \Delta_q=e_{X_q}-e_{Y_q}.
\tag{3.1}
\]

The old packet contains the removed occurrence, so
\(\lambda_q(Y_q)\ge1\).  For the collision energy

\[
                         \operatorname{Col}(\lambda)
                         =\sum_S\binom{\lambda(S)}2,
\tag{3.2}
\]

one has

\[
\begin{aligned}
 \operatorname{Col}(\lambda_q+\Delta_q)
 -\operatorname{Col}(\lambda_q)
 &=\lambda_q(X_q)+1-\lambda_q(Y_q)\\
 &=\lambda_q(X_q)-\lambda_q(Y_q)+1.
\end{aligned}
\tag{3.3}

Every floor correction at a fixed rank subtracts a constant and a fixed
linear function of the total load.  The exchange preserves total load,
so (3.3) is also its exact floor-corrected energy change.  This proves
(0.5).

For weights \(w_q\ge0\), the linked all-depth change is exactly

\[
 \sum_{q=1}^H w_q
 \bigl(\lambda_q(X_q)-\lambda_q(Y_q)+1\bigr).
\tag{3.4}
\]

Thus one orientation is a strict descent if and only if the expression
in (3.4) is negative.  Reversing the whole compound move negates the
endpoint energy difference, as it must.

The two isolated packet endpoints have equal floor energy: the global
transposition \((a_0\ a_1)\) maps \(\mathcal O\) to \(\mathcal N\).
Consequently descent comes from the correlation with the ambient load,
not from a hidden self-energy imbalance.  This is the exact charged-cut
quantity that a covering theorem for these seams would have to control.

For completeness, the upper action (2.16) has the exact floor change

\[
 \Phi_q^+(\lambda_q^++\Delta_q^+)-\Phi_q^+(\lambda_q^+)
 =\langle\lambda_q^+,\Delta_q^+\rangle+2,
 \qquad 1\le q<H,
\tag{3.5}
\]

because \(\Delta_q^+\) has two \(+1\)'s, two \(-1\)'s, and squared norm
\(4\). Equations (3.3) and (3.5) therefore give the complete exact
two-sided floor derivative of the untagged exchange.

## 4. Full common-base cubes cannot do this without a moving hole

The preceding construction depends on deleting different boundary
phases in the two abstract words.  We now prove the complementary
rigidity statement.

Let \(d\ge1\).  Take a core \(C\) of size \(M-d\) and pairwise disjoint
label pairs

\[
                         \{x_{r,0},x_{r,1}\}\qquad(1\le r\le d),
\tag{4.1}
\]

outside \(C\).  For \(\varepsilon\in\{0,1\}^d\), put

\[
 U_\varepsilon=C\cup
       \{x_{1,\varepsilon_1},\ldots,x_{d,\varepsilon_d}\}.
\tag{4.2}
\]

An abstract common-base pattern \(\alpha\) is an arbitrary cyclic order
of \(C\cup\{A_1,\ldots,A_d\}\); core labels and placeholders may be
intermixed arbitrarily.  Let \(\alpha_\varepsilon\) be its specialization.
For \(h<M\), let \(D_h(\alpha_\varepsilon)\) be the complete deck of
the complementary \((M-h)\)-interval targets.  Define its alternating
cube deck

\[
 \mathcal A_h(\alpha)
 =\sum_{\varepsilon\in\{0,1\}^d}
   (-1)^{|\varepsilon|}D_h(\alpha_\varepsilon).
\tag{4.3}
\]

For \(K\subseteq C\), put

\[
 \Gamma_K=\sum_\varepsilon(-1)^{|\varepsilon|}
 e_{K\cup\{x_{1,\varepsilon_1},\ldots,
                    x_{d,\varepsilon_d}\}}.
\tag{4.4}
\]

The vectors \(\Gamma_K\) for distinct \(K\)'s have disjoint supports.

Let \(\mathcal Q_h(\alpha)\) denote the family of cyclic length-\(h\)
intervals of \(\alpha\) containing no placeholder.

### Lemma 4.1 (exact cube derivative)

For every pattern \(\alpha\),

\[
 \boxed{\mathcal A_h(\alpha)
       =\sum_{Q\in\mathcal Q_h(\alpha)}\Gamma_{C\setminus Q}.}
\tag{4.5}
\]

#### Proof

Complement a target interval inside its top and call the resulting
length-\(h\) interval \(Q\).  If \(Q\) contains placeholder \(A_r\),
then its complementary target omits \(x_{r,\varepsilon_r}\) and is
independent of \(\varepsilon_r\).  Summing the sign in that coordinate
cancels it.  If \(Q\) contains no placeholder, its target is

\[
 (C\setminus Q)\cup
 \{x_{1,\varepsilon_1},\ldots,x_{d,\varepsilon_d}\},
\]

and its alternating sum is exactly \(\Gamma_{C\setminus Q}\). \(\square\)

### Lemma 4.2 (an \(H\)-window deck determines every longer core deck)

Assume \(H\ge2\).  The set family \(\mathcal Q_H(\alpha)\) determines
\(\mathcal Q_h(\alpha)\) for every \(h\ge H\).

#### Proof

The placeholders split the cyclic word into disjoint linear runs of core
labels.  A run of length less than \(H\) contributes no member of
\(\mathcal Q_H\).  For the remaining runs, form the graph whose vertices
are the members of \(\mathcal Q_H\), joining two when their intersection
has size \(H-1\).

Different core runs have disjoint label sets, so no edge joins them.
Inside one run, two distinct \(H\)-windows intersect in \(H-1\) labels
if and only if their starts are consecutive.  Hence every nontrivial
component is the path of consecutive \(H\)-windows in one core run; a run
of length exactly \(H\) gives an isolated vertex.

Let \(E_1,\ldots,E_k\) be one recovered path, in either direction.  A
length-\(h\) core interval in this run is exactly

\[
                         E_j\cup E_{j+1}\cup\cdots\cup
                         E_{j+h-H}
\tag{4.6}
\]

for a block of \(h-H+1\) consecutive path vertices.  Conversely every
such union is a length-\(h\) interval.  Formula (4.6) is unchanged by
reversing the recovered path.  Runs of length below \(H\) cannot
contribute at any length \(h\ge H\), and isolated \(H\)-runs contribute
only when \(h=H\).  Thus the claimed family is determined. \(\square\)

### Theorem 4.3 (all-dimensional common-base cube rigidity)

Let \(\alpha,\beta\) be arbitrary common-base patterns.  Make the usual
checkerboard compound exchange: one endpoint uses \(\alpha\) on the even
cube vertices and \(\beta\) on the odd vertices, and the other endpoint
reverses these choices.  If this exchange preserves the complete middle
load, then it preserves the complete load at every lower depth
\(q\ge0\).

The same conclusion holds after deleting one common positional phase
whose alternating phase contribution vanishes in both patterns.  It does
not apply to the pattern-dependent moving holes of Theorem 2.1.

#### Proof

The aggregate change at complementary length \(h\) is

\[
                         \mathcal A_h(\beta)-
                         \mathcal A_h(\alpha).
\tag{4.7}
\]

At the middle row \(h=H\), its vanishing and the disjoint supports of
the \(\Gamma_K\)'s imply

\[
                         \mathcal Q_H(\alpha)
                         =\mathcal Q_H(\beta)
\tag{4.8}
\]

as multisets.  Lemma 4.2 gives equality of \(\mathcal Q_h\) for every
\(h\ge H\), and Lemma 4.1 then makes (4.7) zero for every such \(h\).
Putting \(h=H+q\) proves the lower-depth assertion.

If a common deleted phase has zero alternating contribution, deleting it
does not change either side of (4.7), so the same proof applies. \(\square\)

The theorem covers every full \(2^d\)-top multilinear cube, including
the \(d=2\) quartet and \(d=3\) eight-top cube.  The two abstract words
may move placeholders through the core, so it also covers mixed
core--placeholder positional patterns.  What it does not cover is a
non-cube six-top circuit, vertex-dependent pattern choices not arising
from one checkerboard derivative, or unequal moving holes.

## 5. Exact boundary

Proved here:

1. a two-top exchange of four literal one-hole frame columns;
2. exact preservation of the complete retained middle-owner load, together
   with the exact count \(H-1\) of internal repeated owners at either
   endpoint;
3. one nested unit transfer at every lower depth \(1\le q\le H\);
4. exact lower action \(2H\), exact upper action \(4(H-1)\), and exact
   two-sided untagged action \(6H-4\);
5. the exact floor-energy changes (3.3)--(3.5) and strict-descent
   criterion;
6. rigidity of every full common-base checkerboard cube in arbitrary
   dimension; and
7. the precise reason the positive primitive escapes that rigidity: its
   two deleted boundary phases are different and move with the frame.

Not proved here:

1. a squarefree collar eliminating the \(H-1\) internal repeats while
   retaining the nonzero lower action;
2. that every state with \(\Omega(W)\) floor energy contains enough
   favorably oriented copies of the two-top seam;
3. simultaneous owner-disjoint packing of a dense family of these seams;
4. preservation of an arbitrary preassigned nested tag schedule;
5. a positive-density realization inside the fixed mechanical support;
   or
6. coefficient one.

The next exact statements are, in order: first construct a bounded collar
which resolves the \(H-1\) common middle owners without cancelling the
nested transfer, and then prove a charged seam-cover theorem for the
resulting squarefree circuit. The desired cover must capture a positive
fraction of the current overload with the linked charge in (3.4)
negative. Unlike the quartet holonomy, the bare primitive already has the
correct nonzero floor derivative; its unresolved defect is squarefree
middle-owner realization, not all-depth action.
