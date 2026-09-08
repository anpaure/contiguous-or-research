# PBBS in-place replacement: the exact simple-sector certificate obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Outcome

Consider a simple PBBS omitted-label return of gap \(2s+1\), and one of
its two step-two projected owner rows.  The row has only \(s+1\) owner
positions.  Nevertheless its consecutive intersections and unions through
depth \(s\) form a full two-arm grid, and every arbitrary nonzero literal
word representing that grid has length at least

\[
   \boxed{2s+1.}
\tag{0.1}
\]

The central-marker word attains equality.  Thus a self-contained
replacement of the \(s+1\) nonnegative erosion slots belonging to this
row has net excess at least \(s\).  In the critical Gaussian sector
\(s=\Theta(H)\), this is linear in the sector span and is not
\(o(\text{span})\).

There is a precise boundary version.  If the replacement also deletes
\(c\) collar baseline slots, and \(\rho\) of the forced sector
certificates are supplied by positions outside the replacement block, then
its net excess \(\delta\) obeys

\[
   \boxed{\delta\ge s-c-\rho.}
\tag{0.2}
\]

Consequently any net-\(o(s)\) in-place replacement must consume or export
at least \(s-o(s)\) arm certificates.  This is an exact interval/ownership
invariant.  It identifies the only possible local escape: fuse the arm
orders of different sectors, or absorb a linear collar.

The centered PBBS \(q=2\) theorem does not close that escape.  Fewer than
\(24\operatorname{Cat}_m\) rooted lower \(q=2\) occurrences (and fewer
than \(8\operatorname{Cat}_m\) rooted upper occurrences) have a nonunique
target, but occurrence uniqueness refers to the old PBBS owner windows,
not to arbitrary literal witnesses after recoding.  An explicit sliding
collar has completely injective fixed-depth shadows and still admits a
length \(S+H+1\) wholesale replacement.  Hence no global bound on stolen
collar slots follows from \(q=2\) uniqueness alone.

The result is a rigorous no-go for independent sector-local replacement.
It is not a no-go for a common cross-sector or cross-parity braid.

## 1. The exact PBBS fixed-core row

Let

\[
 A_{t+1}=[2r+1]\setminus(A_t\cup\{\lambda_t\})
\tag{1.1}
\]

be the PBBS trajectory.  Suppose

\[
 \lambda_{2s+1}=\lambda_0
\tag{1.2}
\]

and that

\[
 \lambda_0,\lambda_1,\ldots,\lambda_{2s}
\tag{1.3}
\]

are pairwise distinct.  The audited simple-return normal form gives, after
choosing one step-two parity and complementing its rank-\(r\) owners,

\[
 X_j=K'\cup\{\gamma_j,\gamma_{j+1},\ldots,\gamma_{j+s}\},
 \qquad 0\le j\le s,
\tag{1.4}
\]

where

\[
 |K'|=r-s
\tag{1.5}
\]

and \(\gamma_0,\ldots,\gamma_{2s}\) are pairwise distinct and disjoint
from \(K'\).  Every \(X_j\) has rank \(r+1\).

Put

\[
 C=K'\cup\{\gamma_s\},
\tag{1.6}
\]

and define the two arms by

\[
 \ell_i=\gamma_{s-i},\qquad
 \rho_i=\gamma_{s+i},
 \qquad 1\le i\le s.
\tag{1.7}
\]

For \(0\le a,b\le s\), set

\[
 T_{a,b}
 =C\cup\{\ell_1,\ldots,\ell_a\}
    \cup\{\rho_1,\ldots,\rho_b\}.
\tag{1.8}
\]

Empty initial segments are omitted.

### Lemma 1.1 (exact intersection/union atlas)

For every \(0\le u\le v\le s\),

\[
 \boxed{
 \bigcap_{j=u}^{v}X_j=T_{s-v,u},
 \qquad
 \bigcup_{j=u}^{v}X_j=T_{s-u,v}.}
\tag{1.9}
\]

Moreover every \(T_{a,b}\), \(0\le a,b\le s\), occurs in (1.9): it is
an intersection when \(a+b\le s\), and a union when \(a+b\ge s\).

#### Proof

The active intervals in (1.4) are ordinary intervals in the displayed
\(\gamma\)-order.  Therefore

\[
 \bigcap_{j=u}^{v}X_j
 =K'\cup\{\gamma_v,\ldots,\gamma_{u+s}\}
 =T_{s-v,u},
\tag{1.10}
\]

and

\[
 \bigcup_{j=u}^{v}X_j
 =K'\cup\{\gamma_u,\ldots,\gamma_{v+s}\}
 =T_{s-u,v}.
\tag{1.11}
\]

If \(a+b\le s\), choose \(u=b\) and \(v=s-a\) in the first formula.
If \(a+b\ge s\), choose \(u=s-a\) and \(v=b\) in the second.  These
choices satisfy \(u\le v\) and give \(T_{a,b}\). \(\square\)

The rank is

\[
 |T_{a,b}|=r-s+1+a+b.
\tag{1.12}
\]

Thus the whole atlas lies between ranks \(r-s+1\) and \(r+s+1\), namely
within signed depth \(s\) of the owner rank \(r+1\).  A Gaussian compiler
with \(H\ge s\) is required to cover all of it.

## 2. Sharp arbitrary-word lower bound

### Theorem 2.1 (two-arm certificate theorem)

Every nonzero literal word representing all sets \(T_{a,b}\) in (1.8)
has length at least \(2s+1\).

#### Proof

Choose a witnessing interval for \(T_{0,0}=C\).  Every letter in that
interval is a nonempty subset of \(C\).  Choose one of its positions and
call it \(N\).

For each \(1\le i\le s\), choose a witness for \(T_{i,0}\).  Some
letter in this witness contains \(\ell_i\); choose one such position and
call it \(E_i\).  Since every letter in the witness is a subset of
\(T_{i,0}\), the letter at \(E_i\)

* contains \(\ell_i\);
* contains no \(\rho\)-label; and
* contains no \(\ell_j\) with \(j>i\).

The positions \(E_1,\ldots,E_s\) are distinct.  Indeed, if \(i<j\),
then the letter at \(E_j\) contains \(\ell_j\), while the letter at
\(E_i\) excludes \(\ell_j\).

Similarly, from witnesses for \(T_{0,j}\), choose positions \(F_j\)
whose letters contain \(\rho_j\).  The \(F_j\)'s are pairwise distinct,
contain no \(\ell\)-label, and hence are distinct from every \(E_i\).
The neutral position \(N\) contains no arm label and is distinct from all
\(E_i,F_j\).  We have found

\[
 1+s+s=2s+1
\]

distinct word positions. \(\square\)

The bound is sharp: the central-marker word

\[
 \boxed{
 \{\ell_s\},\ldots,\{\ell_1\},
 C,
 \{\rho_1\},\ldots,\{\rho_s\}}
\tag{2.1}
\]

has length \(2s+1\), and the interval consisting of its last \(a\) left
arm positions, its central position, and its first \(b\) right arm
positions has union exactly \(T_{a,b}\).

No chronological-owner, fixed-witness, rank-homogeneity, or helper-letter
hypothesis was used in the lower bound.

## 3. Exact collar-consumption and boundary-port inequality

The nonnegative endpoint-capped erosion baseline assigns one position to
each owner of a cut path.  Hence the row (1.4) contributes \(s+1\)
baseline positions.

Consider a splice which deletes those \(s+1\) positions and also deletes
\(c\ge0\) other baseline positions from its collars.  Let \(Z\) be the
inserted replacement block.  For the certificate choices in the proof of
Theorem 2.1, let \(\rho\) be the number of the \(2s+1\) chosen positions
which lie outside \(Z\).  Thus \(\rho\) measures certificates exported to
the unchanged exterior or shared with another block.

### Theorem 3.1 (local replacement budget)

With

\[
 \delta=|Z|-(s+1+c),
\tag{3.1}
\]

one has

\[
 \boxed{|Z|\ge2s+1-\rho,\qquad
        \delta\ge s-c-\rho.}
\tag{3.2}
\]

#### Proof

The proof of Theorem 2.1 supplies \(2s+1\) distinct certificate
positions in the complete final word.  Exactly \(\rho\) were declared
outside \(Z\), so at least \(2s+1-\rho\) lie in \(Z\).  Subtracting the
\(s+1+c\) deleted baseline positions gives (3.2). \(\square\)

For a self-contained sector chart \(\rho=0\).  If it does not consume a
linear collar, \(c=o(s)\), then

\[
 \delta\ge(1-o(1))s.
\tag{3.3}
\]

At critical saturation the simple sectors have \(s=\Theta_A(H)\).
Therefore independent sector-local replacement has a positive linear toll.

Theorem 3.1 also states exactly how this conclusion can fail: a
near-zero-net compiler must have

\[
 c+\rho\ge s-o(s).
\tag{3.4}
\]

It must absorb a linear number of neighbouring baseline positions, or
make a linear number of arm certificates genuinely nonlocal.

## 4. The certificate-overlap problem for many sectors

The preceding proof can be expressed as an exact statewise compatibility
problem.  For one sector define the following classes of possible literal
letters:

\[
 \mathcal N=\{Z:\varnothing\ne Z\subseteq C\},
\tag{4.1}
\]

\[
 \mathcal E_i
 =\left\{Z:\ell_i\in Z\subseteq
 C\cup\{\ell_1,\ldots,\ell_i\}\right\},
\tag{4.2}
\]

\[
 \mathcal F_j
 =\left\{Z:\rho_j\in Z\subseteq
 C\cup\{\rho_1,\ldots,\rho_j\}\right\}.
\tag{4.3}
\]

Every word covering the grid contains a letter in every one of these
\(2s+1\) classes, and the classes belonging to one sector are pairwise
disjoint.

For classes from several sectors, write a nonneutral class as a pin-cap
pair \((p,U)\): every member contains \(p\) and is a subset of \(U\).
A collection \((p_\alpha,U_\alpha)\) admits one shared literal letter if
and only if

\[
 \boxed{
  \{p_\alpha:\alpha\}\subseteq
       \bigcap_\alpha U_\alpha.}
\tag{4.4}
\]

Necessity is immediate.  For sufficiency, use the union of the pins as the
shared letter.  A collection of neutral classes is compatible exactly when
the corresponding cores have nonempty intersection; mixed neutral and
pin-cap classes have the evident combined condition.

Thus global in-place fusion is reduced to a concrete PBBS pin-cap overlap
theorem.  Projected-edge disjointness of the return traces does not by
itself bound the overlap multiplicity in (4.4), because it imposes no
corresponding disjointness on the large cores or axis caps.

## 5. Exact relation with centered \(q=2\) chronology

In the uncomplemented even row, write

\[
 A_j^E
 =K\cup\{a_0,\ldots,a_{j-1}\}
       \cup\{b_j,\ldots,b_{s-1}\}.
\tag{5.1}
\]

Its consecutive \(q=1\) colors are

\[
 R_j=A_j^E\cap A_{j+1}^E.
\tag{5.2}
\]

For \(1\le j\le s-1\), the centered \(q=2\) target is

\[
 S_j=A_{j-1}^E\cap A_j^E\cap A_{j+1}^E
 =K\cup\{a_0,\ldots,a_{j-2}\}
      \cup\{b_{j+1},\ldots,b_{s-1}\}.
\tag{5.3}
\]

Exactly,

\[
 \boxed{R_{j-1}=S_j\cup\{b_j\},\qquad
        R_j=S_j\cup\{a_{j-1}\}.}
\tag{5.4}
\]

Hence the consecutive \(q=1\) facets meet in their \(q=2\) core by the
literal exchange \(b_j\leftrightarrow a_{j-1}\).  The sets \(S_j\) are
pairwise distinct.  This is the fixed-core specialization of the audited
parenthesis-block chronology.

The centered factor also satisfies

\[
 1\le\mu_2^-(S)\le10,
 \qquad
 1\le\mu_2^+(U)\le3.
\tag{5.5}
\]

The two excess occurrence masses are

\[
 E_2^-:=\sum_S(\mu_2^-(S)-1)
 =W-\binom{2m+1}{m-2}
 <12\operatorname{Cat}_m.
\tag{5.6a}
\]

and

\[
 E_2^+:=\sum_U(\mu_2^+(U)-1)
 =W-\binom{2m+1}{m+2}
 ={2W\over m+2}
 <4\operatorname{Cat}_m.
\tag{5.6b}
\]

Let \(U_2^-\) and \(U_2^+\) be the numbers of rooted signed \(q=2\)
occurrences whose target occurs at least twice in the centered PBBS factor.
Since

\[
 \mu\le2(\mu-1)\qquad(\mu\ge2),
\]

equations (5.6a)--(5.6b) give the exact bounds

\[
 \boxed{U_2^-<24\operatorname{Cat}_m,
        \qquad U_2^+<8\operatorname{Cat}_m.}
\tag{5.7}
\]

Thus almost every original centered \(q=2\) occurrence is unique.

This does not bound \(c\) or \(\rho\) in Theorem 3.1.  The reason is
logical, not heuristic: \(\mu_2\) counts rooted PBBS owner windows, whereas
a replacement may create a new literal interval for the same target.  In
the complemented grid (1.8), lower signed depth \(q\) is the diagonal

\[
 a+b=s-q.
\tag{5.8}
\]

The upper signed depth \(q\) is the diagonal \(a+b=s+q\).  The
certificate proof needs both axis chains for all \(1\le i\le s\).  At
\(q=2\), the lower diagonal meets at most the two axis classes with
\(i=s-2\) (and meets none when this index is outside \([1,s]\)); the
upper diagonal meets no axis class.  Therefore even perfect two-sided
\(q=2\) uniqueness controls at most two of the \(2s+1\) certificate
classes of a sector.

## 6. A statewise counterexample to collar rigidity from uniqueness

Fix a nonempty set \(G\), distinct coordinates

\[
 \eta_0,\eta_1,\ldots,\eta_{S+H},
\]

and the Johnson path

\[
 Y_i=G\cup\{\eta_i,\eta_{i+1},\ldots,\eta_{i+H}\},
 \qquad0\le i\le S.
\tag{6.1}
\]

For \(0\le q\le H\),

\[
 \bigcap_{t=0}^{q}Y_{i+t}
 =G\cup\{\eta_{i+q},\ldots,\eta_{i+H}\},
\tag{6.2}
\]

and

\[
 \bigcup_{t=0}^{q}Y_{i+t}
 =G\cup\{\eta_i,\ldots,\eta_{i+H+q}\}.
\tag{6.3}
\]

For every fixed \(q\), the targets in (6.2) are pairwise distinct as
\(i\) varies.  Nevertheless the word

\[
 G\cup\{\eta_0\},
 G\cup\{\eta_1\},\ldots,
 G\cup\{\eta_{S+H}\}
\tag{6.4}
\]

has length \(S+H+1\) and represents (6.2) by positions
\(i+q,\ldots,i+H\), and (6.3) by positions
\(i,\ldots,i+H+q\).  It retains none of the original owner letters when
\(H\ge1\).

If \(S/H\to\infty\), its overhead \(H\) is \(o(S)\), despite exact
fixed-depth injectivity and simultaneous all-depth coverage.  This is a
rigorous counterexample to every inference from shallow occurrence
uniqueness alone to physical baseline-slot rigidity.  It is not asserted
to be a PBBS trajectory; it proves that any negative PBBS theorem must use
additional PBBS chronology.

## 7. Exact implication boundary

The following is proved.

1. A simple return row of projected residence \(s+1\) needs exactly
   \(2s+1\) letters when compiled self-contained through its full depth.
2. Replacing only its \(s+1\) erosion baseline cells costs at least \(s\)
   net letters.
3. A net-\(o(s)\) local replacement must consume or export
   \(s-o(s)\) forced certificates.
4. The centered \(q=2\) uniqueness theorem does not bound that export.

The following is not proved and is not refuted.

* A common replacement block may share arm certificates among many
  sectors satisfying the pin-cap condition (4.4).
* Sharing the two step-two parities in a circular packet can evade the
  one-parity count, but converting such circular sharing into a global
  linear word while preserving the original crossing targets requires
  additional literal port and owner compatibility.
* A long PBBS block may admit a changing-witness compiler analogous to the
  sliding collar in Section 6.

Therefore critical packing definitively kills an independent local
in-place compiler, just as it kills the append-only clustered compiler.
The surviving coefficient-one gate is an exact cross-sector certificate
overlap theorem: on a positive-density double-deck packing, construct a
common literal arm braid with only \(o(\sum s)\) unshared certificates, or
prove from PBBS parenthesis chronology that condition (4.4) has
insufficient aggregate overlap.
