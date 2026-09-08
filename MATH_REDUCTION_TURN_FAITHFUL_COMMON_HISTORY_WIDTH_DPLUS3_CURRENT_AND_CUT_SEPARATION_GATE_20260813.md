# Turn-faithful common histories carry the selected `q2` current at width `d+3`

**Date:** 2026-08-13  
**Status:** exact two-turn local current theorem and exact global
cut-separation gate.
It extends the common-intersection source lift by one owner.  It does not
assert that the required three-owner fragments are already planted in the
canonical MSW source chronology.

## 1. A changed hinge with its untouched mate

Fix source depth `d>=1` and owner rank `R`.  Let a changed oriented owner
transition have old form

\[
                         A_i\longrightarrow B_i
\]

and new form

\[
                         A_i\longrightarrow B_{\pi(i)}.
\]

Assume it is preceded by an unchanged owner occurrence `E_i`, with the
transition `E_i -> A_i` literal in both states.  At owner level the
three-owner turn current is

\[
 E_i\cup A_i\cup B_i
       \longmapsto
 E_i\cup A_i\cup B_{\pi(i)}.                      \tag{1.1}
\]

In the owner--q1 incidence notation, write

\[
 Q_i^-=A_i\cup B_i,
 \qquad Q_i^+=A_i\cup B_{\pi(i)},
 \qquad M_i=E_i\cup A_i.
\]

Then (1.1) is exactly

\[
                         M_i\cup Q_i^-
             \longmapsto M_i\cup Q_i^+.             \tag{1.2}
\]

Thus `M_i` is the untouched q1 mate at `A_i`, and (1.2) is the selected
MSW `q2` turn ledger used by the counter-carry search.

## 2. Source realization

Suppose the hinge `A_iB_i` is realized by a literal common-history
fragment

\[
                 (X_i,C_1,\ldots,C_d,Y_i),          \tag{2.1}
\]

with `H=C_1 dotcup ... dotcup C_d`,

\[
                         H\cup X_i=A_i,
 \qquad                 H\cup Y_i=B_i.              \tag{2.2}
\]

Require one additional source letter `Z_i` immediately before `X_i` such
that the length-`d+1` window ending immediately before `B_i` has owner
`E_i`; equivalently, the three consecutive length-`d+1` owner windows on
the source block

\[
                 Z_i,X_i,C_1,\ldots,C_d,Y_i         \tag{2.3}
\]

are precisely

\[
                         E_i,A_i,B_i.                \tag{2.4}
\]

The full width-`d+3` interval displayed in (2.3) has value

\[
                         E_i\cup A_i\cup B_i.        \tag{2.5}
\]

Cut immediately before each tagged `Y_i` and transport its complete
residual path according to `pi`.  Keep the entire left block through
`Z_i,...,C_d` fixed.  The new full interval has value

\[
                         E_i\cup A_i\cup B_{\pi(i)}. \tag{2.6}
\]

This realizes (1.1) literally.

There is a second changed width-`d+3` interval at the same cut.  Let
`Q_i` be the first source letter after `Y_i` in its complete residual,
and let

\[
                         G_i=C_2\cup\cdots\cup C_d
                              \cup Y_i\cup Q_i                 \tag{2.7}
\]

(with the evident empty `C_2,...,C_d` range when `d=1`).  Thus `G_i` is
the owner immediately after `B_i`.  The interval beginning at `X_i` has
the three-owner value

\[
                         A_i\cup B_i\cup G_i.                  \tag{2.8}
\]

After moving the complete residual indexed by `pi(i)`, its value is

\[
                         A_i\cup B_{\pi(i)}\cup G_{\pi(i)}.    \tag{2.9}
\]

Equations (2.5)--(2.6) and (2.8)--(2.9) are respectively the
predecessor-side and successor-side turns at the moved residual.

## 3. Exact current theorem

### Theorem 3.1

Let a finite bank of fragments (2.3) be occurrence-disjoint.  Assume:

1. every tagged `Y` residual is moved as one complete path;
2. every predecessor transition `E_i -> A_i` is literal and fixed, and
   every successor transition `B_i -> G_i` stays inside the transported
   complete residual;
3. the changed cuts are cyclically separated by at least `d+3` source
   positions.

Then the complete signed change in the source width-`d+3` row is

\[
 \boxed{
   \Delta_2(T)=
   \sum_i\bigl[
      \mathbf 1_{E_i\cup A_i\cup B_{\pi(i)}=T}
     -\mathbf 1_{E_i\cup A_i\cup B_i=T}
     +\mathbf 1_{A_i\cup B_{\pi(i)}\cup G_{\pi(i)}=T}
     -\mathbf 1_{A_i\cup B_i\cup G_i=T}
             \bigr].}                              \tag{3.1}
\]

Consequently an aggregate support-monotone **two-sided** turn ledger
remains support-monotone after the source lift.  In particular, a
support-monotone predecessor ledger suffices when the successor-side
summand is separately support-preserving.  The same rethread preserves
every strict-lower occurrence and is positively `(d+1)`-resident, as in
the common-intersection theorem.

#### Proof

Separation ensures that a width-`d+3` interval meets at most one changed
cut.  At that cut, the interval starting exactly at `Z_i` has old and new
values (2.5)--(2.6), while the interval starting exactly at `X_i` has old
and new values (2.8)--(2.9).  An interval starting before `Z_i` ends
before the tagged `Y` and therefore does not cross this cut.  Every
crossing interval starting at `C_1` or later is a literal interval of the
common history followed by the transported complete residual: since the
ordered `C_1,...,C_d` word is common to all fragments, it is paired with
the identical interval at the residual's old location.  Intervals
avoiding all cuts stay literal inside residual paths.  These classes are
disjoint and exhaustive, proving (3.1).

The strict-lower and positive-residence assertions use exactly the
common-intersection occurrence bijection and cyclic source-occurrence
argument.  \(\square\)

## 4. Sharp separation boundary

The `d+3` separation is a clean sufficient condition, not a cosmetic one.
Under only the shorter cut-separation used for strict-lower transport, a
width-`d+3` interval may meet two changed cuts.  Its value then depends on
two head assignments and is not represented by the sum of the individual
turn currents (3.1).  A denser bank can still be valid, but it must audit
the full joint width-`d+3` cut current rather than summing local ledgers.

The successor-side summand in (3.1) is substantive.  The crossing
interval which starts at `X_i` contains the changed hinge and one source
letter following `Y`; at owner level it is the turn at the `B` endpoint.
It is not automatically literal under an arbitrary head permutation.
Thus the old one-sided predecessor formula is exact only after proving
that this second summand vanishes or is separately support-preserving.
Equivalently, a source lift of a finite incidence packet must carry both
fixed endpoint mates, or audit its full joint two-turn ledger.

For the oriented `T_2` relay, every toggled incidence has unchanged
endpoint mates in the complete finite owner-path ledger.  What remains to
be proved for a source planting is that the two-sided fragments can be
chosen occurrence-disjoint with condition 3 and with the signed current
(3.1) equal to the finite counter-carry ledger, or else that their actual
joint cut current is support-monotone by a direct replay.  Intervals
crossing the z-present complementary return are likewise outside this
local theorem.
