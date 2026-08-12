# Audit of the triangular block-record transfer and the overlap exponents

Date: 2026-07-25  
Method: pure mathematics only

## 0. Verdict

The triangular record transfer in
`PBBS_TWO_DIM_CARRIER_TRANSFER_COUNTEROBSTRUCTION_20260725.md` is exact,
apart from two harmless endpoint/terminology points recorded below.  Its
powers and resolvent really telescope.  The audit has two conclusions.

1. Conditioning on the common outer carrier

   \[
   O=(0S_s)E
   \]

   and on any block state determined by its parsing does **not** destroy the
   \(O(s^{-2})\) coefficient anti-concentration from
   `PBBS_SHARED_BOUNDARY_COLLISION_20260725.md`.  The untouched low-index
   forward blocks still supply the same independent convolution.  The same
   remains true if one additionally fixes an intermediate renewal state
   using dual-array data only.

2. This does not yield an overlap improvement.  In the full corridor the
   initial and terminal first-passage pieces reset the record state.  The
   physical sink consequently accepts every intermediate block state, and
   summing those states gives exactly the old scalar Green factor

   \[
   {1\over1-zC_b(z)C_A(z)}.
   \]

   Its critical mass is \(\Theta(s)\) at a central seam.  Thus a state is
   prescribed for each *fixed* carrier, but the enumeration must sum over
   all prescribed states, and that sum restores the entire critical mode.

Consequently neither

\[
 \Lambda=o(r^{2/5})
 \qquad\hbox{nor}\qquad
 \Lambda=o(r^{1/3})
\]

follows from the triangular record transfer, even after combining it with
the shared-boundary collision theorem.  The currently proved uniform
packing range remains \(\Lambda=o(r^{1/5})\).  This is an obstruction to
the proposed proof of the stronger exponents, not a counterexample to a
future PBBS theorem using additional chronology or packing information.

## 1. Audit of the exact triangular transfer

The marked extension mass preceding the renewal is

\[
 \Xi_{\ell,J}
 ={(\ell+2)(J+1)\over(\ell+1)(J+2)}.
\]

The displayed upper bound \(\Xi_{\ell,J}\le4/3\) in the source note needs
\(\ell\ge2\), not merely \(\ell\ge1\): for \(\ell=1\) and \(J\to\infty\)
the expression tends to \(3/2\).  The genuine common-boundary
\(\ell=1\) sector is empty (both endpoint letters must be zero), so this
minor correction has no asymptotic effect.

Let a lower seam loop have maximum downward depth \(h\), and suppose that
the incoming record is \(p\).  The new record is

\[
 p'=\max\{p,h\}.
\]

With \(A=s-u\), \(b=u-1\), and

\[
 D_h=C_h-C_{h-1},\qquad C_{-1}=0,
\]

one renewal pair has the marked matrix

\[
 R_{p,p}=zC_A C_p,
 \qquad
 R_{p,q}=zC_A(C_q-C_{q-1})y^{q-p}\quad(q>p).
\tag{1.1}
\]

Put \(\lambda_q=zC_A C_q\).  For \(k\ge1\), the total series of all
\(k\)-tuples whose final record is at most \(q\) is \(\lambda_q^k\).
Subtracting the corresponding series at \(q-1\) proves

\[
 (R^k)_{p,q}=
 \begin{cases}
  \lambda_p^k,&q=p,\\
  (\lambda_q^k-\lambda_{q-1}^k)y^{q-p},&q>p,\\
  0,&q<p.
 \end{cases}
\tag{1.2}
\]

Therefore

\[
 [(I-R)^{-1}]_{p,q}=
 \begin{cases}
  (1-\lambda_p)^{-1},&q=p,\\
  (1-\lambda_q)^{-1}-(1-\lambda_{q-1})^{-1},&q>p,\\
  0,&q<p,
 \end{cases}
\tag{1.3}
\]

with the marker \(y^{q-p}\) restored in the second line.  At \(z=1/4\),

\[
 [(I-R)^{-1}]_{p,p}
 ={(A+2)(p+2)\over A+p+3}\le p+2,
\tag{1.4}
\]

and, for \(q>p\),

\[
 [(I-R)^{-1}]_{p,q}
 ={(A+2)(A+1)\over(A+q+3)(A+q+2)}\le1.
\tag{1.5}
\]

These calculations are correct.  Notice, however, that (1.5) is a bound
for one prescribed final record.  It is not a bound for the union of all
positive displacements.

## 2. What conditioning preserves

Let

\[
 d_D=-\min H_{\operatorname{rev}E},
 \qquad d_F=-\min H_E.
\]

These are respectively the dual and forward record depths and need not
be equal.  In the increasing-cap chamber, the exact prefix formula is

\[
 \Pr(\mathscr D_L\hbox{ begins with }w)
 =2^{1-|w|}{L-\operatorname{net}(w)+1\over L+2}.
\tag{2.1}
\]

For \(B=\operatorname{rev}E\) and
\(W_S=\operatorname{rev}(S_s)0\), it gives

\[
 \Pr(W_S\mid B)
 =2^{-|S_s|-1}{\ell+2\over\ell+1}.
\tag{2.2}
\]

In particular, once \(E\) and \(S_s\) are fixed, the record state after
\(BW_S\) is fixed:

\[
 p=\max\{d_D,\operatorname{ht}(S_s)\}-1
\tag{2.3}
\]

up to the convention of sampling immediately before or after the final
zero.

The coefficient issue is separate.  Parsing \(E\) from the forward side
uses only

\[
 S_{s-1},S_{s-2},\ldots,S_{s-d_F}
\]

(the last one only through a prefix).  Hence

\[
 S_1,\ldots,S_{s-d_F-1}
\tag{2.4}
\]

remain independent capped Dyck blocks.  Fixing \(S_s\), fixing any dual
blocks, or fixing a state measurable from those dual blocks does not alter
their law.  Their partition function is the same
\(P_{s,\ell,d_F}\) used in Lemma 3.1 of the shared-boundary note.  Since
\(d_F\le\ell\le cs\), its normalized coefficient distribution has largest
atom \(O(s^{-2})\).  Adding all already fixed lengths and convolving with
all other unfixed blocks cannot increase that largest atom.

Thus the following limited statement is valid:

> For every fixed admissible \(E,S_s\), and every fixed renewal state
> specified without inspecting the blocks in (2.4), the conditional total
> semilength distribution retains the \(O(s^{-2})\) atom bound.

There is an important boundary to this statement.  If by "full carrier"
one means the entire word

\[
 W=R_sOR_0,
\]

then fixing \(R_0\) together with \(E\) fixes

\[
 U=ER_0=(0S_{s-1})\cdots(0S_1).
\]

The convolution (2.4) is then fixed rather than random, so its
anti-concentration cannot be invoked.  The useful conditioning is on
\(O=(0S_s)E\) and dual-side state data, not on all of \(W\).

## 3. Exact reset and telescoping obstruction

Write a forward corridor from height \(s\) to zero as

\[
 F_A\,0\,
 (L_1\,1\,U_1\,0)\cdots(L_k\,1\,U_k\,0)F_b,
 \qquad A=s-u,\quad b=u-1.
\tag{3.1}
\]

In reversed carrier order this is

\[
 \operatorname{rev}F_b\,
 (0\operatorname{rev}U_k1\operatorname{rev}L_k)\cdots
 (0\operatorname{rev}U_11\operatorname{rev}L_1)\,
 0\operatorname{rev}F_A.
\tag{3.2}
\]

If a word has all prefix nets at least \(-d\), has total net \(-d\),
and is appended from height \(p\le d\) above the current record, then its
endpoint is a new record and the final unmatched height is zero.  Both
outer pieces in (3.2) have this reset property.  (The reverse of a first
passage need not itself make its *first* visit to the final minimum at its
last bit; that stronger and unnecessary wording should be avoided.)

After the first reset, the reversed renewal pairs have running-maximum
states \(0\le q\le A+1\).  Put

\[
 \widehat\lambda_q=zC_bC_{q-1}\quad(q\ge1),
 \qquad \widehat\lambda_0=0.
\]

The exact Green entries from state zero are

\[
 \widehat G_{0,0}=1,
 \qquad
 \widehat G_{0,q}
 ={1\over1-\widehat\lambda_q}
  -{1\over1-\widehat\lambda_{q-1}}\quad(q\ge1).
\tag{3.3}
\]

The terminal reset accepts every \(q\).  Therefore

\[
 \boxed{
 \sum_{q=0}^{A+1}\widehat G_{0,q}
 ={1\over1-zC_bC_A}.}
\tag{3.4}
\]

This is the unrestricted scalar seam-renewal factor, coefficientwise.
At \(z=1/4\) and a central seam it is \(\Theta(s)\).

More explicitly, for \(q\ge1\),

\[
 \widehat G_{0,q}(1/4)
 ={(b+2)(b+1)\over(b+q+2)(b+q+1)}.
\tag{3.5}
\]

When \(b\asymp s\), there are \(\Theta(s)\) values
\(q\asymp s\), each with mass \(\Theta(1)\).  Hence

\[
 \sum_{q\ge1}\widehat G_{0,q}(1/4)=\Theta(s).
\tag{3.6}
\]

This proves precisely why "the final state is prescribed" is not enough:
it is prescribed after selecting one carrier, whereas the counting theorem
must sum over all carriers and hence over all \(q\).

## 4. Threshold ledger

The shared-boundary theorem gives, uniformly in its domain,

\[
 z_{r,s,2\ell}
 \le C4^r{(\ell+2)^{3/2}\over s^6}.
\tag{4.1}
\]

For \(s\asymp\sqrt r\), summing over \(s\) and
\(1\le\ell\le L\) gives

\[
 C_A4^r{L^{5/2}\over r^{5/2}}.
\tag{4.2}
\]

Since \(B_r/\sqrt r\asymp4^r/r^2\), (4.2) is little-oh precisely in the
currently proved range

\[
 L=o(r^{1/5}).
\tag{4.3}
\]

Fixing one positive-displacement state contributes at most a constant by
(1.5), but gives no negative power of \(\ell\).  Summing the admissible
states restores \(\Theta(s)\) by (3.4)--(3.6).  A zero-displacement state
has either constant mass after the reset, or, in the unreversed local
orientation, mass as large as \(\Theta(s)\) at a macroscopic incoming
record.  Again there is no negative power of \(\ell\).

For comparison, improving (4.3) to \(L=o(r^{1/3})\) by this summation
scheme would require an additional uniform factor of order
\(\ell^{-1}\) in (4.1).  Improving it to \(L=o(r^{2/5})\) would require,
at the level of the aggregate \(\ell\)-sum, a gain of order
\(L^{-5/4}\) (equivalently a per-height power comparable to
\(\ell^{-5/4}\)).  No such factor appears in (1.3), (2.2), or (3.4).

Therefore the two stronger overlap thresholds are not established.  Any
valid improvement must use information not present in the one-seam
triangular record transfer: a second non-aligned chronological phase,
an actual-PBBS restriction on the scalar Green sector, or a
quotient-edge-disjoint packing argument.
