# K16 H2 outside-R19 low-debt donor and two-return theorem

Date: 2026-07-30  
Lane: A  
Status: exact catalogue, exact maximal-envelope port census, and proved no-go for the stated face

## 1. Scope and frozen source

All positions are zero-based. The source is

~~~text
scratch/k16_ejection_lns_h2_p110_20260730.word
SHA-256 5234b77101ac1f22ec1802b4e1f5eccb6f0fc6f540efff9bbd0dc92da8c09fe7
~~~

of length \(12873\). Its holes are

\[
 P=0x4879,\qquad Q=0x6879,
\]

and \(E=0x082a\) has multiplicity one, with unique witness at position
\(5462\).

Call \(r\gets x\) a nonprovider \(E\)-reserve donor when it creates a second
\(E\)-witness while \(P,Q\) remain holes. Its collateral debt is the set of
previously covered masks whose exact multiplicity becomes zero.

The return catalogue is the same fixed-service \(R19\) catalogue as in the
preceding theorem:

\[
\begin{aligned}
B_1&=[576,578],&B_2&=[3329,3331],&B_3&=[3494,3496],\\
B_4&=[3838,3840],&B_5&=[5463,5466],&B_6&=[5971,5973].
\end{aligned}
\]

The service cell \(5462\) is not a return cell.

## 2. Complete low-debt donor catalogue

**Theorem 2.1 (outside-\(R19\) catalogue).** Among every nonprovider
\(E\)-reserve donor in the authenticated atlas, exactly \(31\) have
collateral size at most one. Two lie inside \(R19\):

\[
\begin{array}{c|c|c}
r&x&\text{debt}\\\hline
578&0x082a&0x082b\\
3839&0x082a&0x0862.
\end{array}
\]

Exactly \(29\) lie outside \(R19\). One of these is

\[
0:0x2c61\longmapsto0x082a,\qquad \text{debt }0x2c6d. \tag{2.1}
\]

It is catalogued but quarantined: (2.1) is the already-owned
H1/four-portal branch, and including it here would duplicate that
four-edit lane.

The operative ordinary catalogue therefore has \(28\) rows:

1. the nine zero-debt donors
   \[
   r\in\{573,3044,3644,6090,6302,6725,10082,10277,10881\},
   \qquad x=0x082a;
   \]
2. the following nineteen fresh one-debt donors:

   (Positions are decimal; value and debt columns are hexadecimal.)

\[
\begin{array}{r|r|r@{\qquad}r|r|r}
r&x&\text{debt}&r&x&\text{debt}\\\hline
226&082a&090a&287&082a&082e\\
2346&082a&0826&4311&082a&092a\\
4443&082a&0a2a&5881&082a&08aa\\
6664&082a&890a&7011&082a&8a0a\\
7016&082a&882b&7373&082a&982a\\
8784&082a&882e&9482&082a&882a\\
9933&000a&c86a&9933&002a&c86a\\
10749&082a&892a&11900&082a&c86b\\
12319&082a&88aa&12528&082a&880a\\
12740&082a&840a&&&
\end{array}
\]

*Proof.* The frozen reserve atlas exhausts every nonzero value capable of an
\(E\)-witness at every source position, evaluates its complete interval
multiplicity delta, and filters by \(E\)-multiplicity at least two and
\(P,Q\)-multiplicity zero. Filtering its accepted rows by collateral at
most one and the displayed position conditions gives the stated counts.
The canonical compact-JSON hashes are

\[
\begin{array}{c|c}
\text{filter}&\text{SHA-256}\\\hline
\text{outside }R19\text{ including }p0&
02a210de2cf80b36c586a67be5933f2b14dc81ead42a1a2d7013d19ef4b23b5f\\
\text{operative 28}&
28f6681819a40ff39d854d9ff01d3898da0d8cbe34acc81c6b55953dd408c585\\
\text{fresh one-debt 19}&
828336747974939e4159b997e468b9548e3ed8a048d5d43b5bfd05c827611dcd.
\end{array}
\]

The retained catalogue is serialized independently in

~~~text
scratch/threadA_k16_h2_outside_r19_lowdebt_catalogue_20260730.audit.json
~~~

\(\square\)

Fix any operative donor and then replace position \(5462\) by one of

\[
\mathcal Y=\{0018,0038,0058,0078,0818,0838,0858,0878\}. \tag{2.2}
\]

Exact replay gives

\[
\operatorname{holes}
=\{0x486b,0x686b,0x6c6b\}\cup D(r,x), \tag{2.3}
\]

where \(D(r,x)\) is the donor debt. Thus the nine inherited donors give the
previous \(72\) three-hole bases, while the nineteen fresh donors give
\(19\cdot8=152\) four-hole bases. There are eighteen distinct fresh hole
sets; the two alleles at position \(9933\) share the same debt.

## 3. Maximal-envelope return ports

Let \(V\) be one of the fresh bases and let \(q\in R19\). For a target \(T\),
delete \(V_q\) and extend in both directions through the maximal consecutive
fixed blocks whose letters are submasks of \(T\). Let their OR be
\(c_q^V(T)\), and put

\[
r_q^V(T)=T\setminus c_q^V(T).
\]

Let \(\mathcal S_q(V)\) be the holes together with every covered target all
of whose witnesses contain \(q\), and define

\[
L_q(V)=\bigvee_{T\in\mathcal S_q(V)}r_q^V(T),\qquad
U_q(V)=\bigcap_{T\in\mathcal S_q(V)}T. \tag{3.1}
\]

The exact one-cell theorem says that changing only \(q\) completes \(V\) if
and only if the Boolean interval

\[
\{y:y\ne0,\ y\ne V_q,\ L_q(V)\subseteq y\subseteq U_q(V)\}. \tag{3.2}
\]

is nonempty.

**Theorem 3.1 (port census).** Across all \(152\cdot19=2888\) fresh
base/port instances, (3.2) is empty. Hence none of the fresh bases has a
one-return completion in \(R19\).

For diagnostics, the exact union of values at \(q\) which individually
provide at least one current hole is

\[
\mathcal P_q(V)=
\bigcup_{H\in\operatorname{holes}(V)}
\{y:y\ne0,\ y\ne V_q,\ r_q^V(H)\subseteq y\subseteq H\}. \tag{3.3}
\]

The complete census has \(527024\) base/port/value incidences and signature

~~~text
8d3a9795f9580663  (ordered FNV-1a-64 diagnostic)
~~~

Every port has a nonempty domain. Across all (2888) base/port instances,
the domain sizes range from (129) to (320). Equation (3.3) is diagnostic
only. It is not
used to restrict the two-return search, because same-block witnesses can
depend jointly on two values even when neither value individually provides
a current hole.

## 4. Exact two-return kernel

Fix return cells \(p<q\). Let

\[
K_{p,q}(V)=
\{T\ne0:\text{no }T\text{-witness avoids both }p,q\}.
\]

Partition the changed intervals into \(p\)-only, \(q\)-only, and both-cell
classes, with exact Boolean profiles

\[
X_T(x),\qquad Y_T(y),\qquad Z_T(x\lor y).
\]

Then the twice-edited word is universal exactly when

\[
X_T(x)\lor Y_T(y)\lor Z_T(x\lor y)=1
\quad(T\in K_{p,q}(V)). \tag{4.1}
\]

The critical set is recomputed from the exact base multiplicities. In
particular the fourth donor debt in (2.3) is never omitted.

**Lemma 4.1 (exact joint-activity test).** Let \(a=V_p,b=V_q\), and let
\(c\) be the fixed-context OR of a both-cell interval. The \(Z\)-profile can
be nonzero on \(T\in K_{p,q}(V)\) for some allowed nonzero
\(x\ne a,y\ne b\) if and only if

\[
c\subseteq T
\quad\text{and}\quad
\bigl(|T|\ge2\ \text{or}\ (T\ne a\text{ and }T\ne b)\bigr). \tag{4.2}
\]

*Proof.* Necessity of \(c\subseteq T\) is immediate. If \(T\) is a
singleton, both nonzero values must equal \(T\), giving the second clause.
If \(|T|\ge2\), allowed submasks whose union is \(T\) always exist: use
\(T\) itself at an endpoint whose incumbent differs, and when both
incumbents equal \(T\), use two proper coatoms whose union is \(T\).
\(\square\)

Thus \(Z\) is dropped only after the actual-base test (4.2), not merely from
nominal block labels. In the authenticated census, all \(22800\) cross-block
kernels are joint-inactive and all \(3192\) same-block kernels are
joint-active. This independently confirms that every modified inter-block
gap still supplies the safe \(0x7fff\) separator.

For a fixed first value \(x\), let \(D_x\) be the targets in (4.1) not yet
covered by \(X\). Any completing \(y\) lies below

\[
T_x=\bigcap_{T\in D_x}T.
\]

Coverage by \(Y(y)\) or \(Z(x\lor y)\) is upward-monotone for
\(y\subseteq T_x\). Therefore it is exhaustive to test \(T_x\), or its
nonzero coatoms when \(T_x\) is the forbidden incumbent. This is the same
proved maximum-envelope/coatom MITM as in the fixed-service theorem.

## 5. Exact decision

**Theorem 5.1 (fresh one-debt no-go).** None of the \(152\) fresh bases can
be completed by changing one or two distinct cells of \(R19\) to arbitrary
allowed nonzero values.

*Proof.* Theorem 3.1 excludes one return. For two returns, the exact engine
exhausts

\[
152\binom{19}{2}=25992
=22800+3192
\]

kernels. These represent

\[
25992\cdot65534=1703359728
\]

raw first-value rows. Exact profile equality reduces the logical ledger to
\(210076616\) first-profile rows and \(207476112\) envelope/coatom tests.
There are \(5346\) exact kernel keys and \(20646\) identity-cache hits. The
largest critical set has size \(37\). Every case has \(171\) kernels, the
final witness is null, and the negative cardinality assertions pass.
\(\square\)

Combining Theorem 5.1 with the preceding zero-debt R19 theorem and its
one-return predecessor theorem gives:

**Corollary 5.2.** No operative donor in the complete \(28\)-row ordinary
outside-\(R19\), collateral-at-most-one \(E\)-reserve catalogue, followed by
one of the eight services (2.2), can be completed with at most two return
edits in \(R19\).

## 6. Authentication

The engine is

~~~text
scratch/search_threadA_k16_h2_outside_r19_onedebt_tworeturn_mitm_20260730.cpp
SHA-256 30f3328ba6359e63b6970dfb5e32efeefdd4f8a983c96026ea333c6001961f97
~~~

and includes the frozen audited R19 kernel source

~~~text
SHA-256 644ff89cba87372db01420ba8c61c1794065e6c1a37c4677bf348d5db3f80fd3.
~~~

Two independent source audits checked the catalogue, exact critical set,
joint-activity predicate, one-cell envelope, cache key, arbitrary-value
envelope reduction, early positive handling, and all counters.

The run used one H100 CPU, /home only, a \(4\) GiB address-space cap, and no
SAT solver. It exited zero after \(6.70\) seconds, used \(9396\) KiB maximum
resident memory, and incurred no swap. A fresh second run produced a
byte-identical audit.

Principal artifacts are

~~~text
scratch/threadA_k16_h2_outside_r19_onedebt_tworeturn_mitm_20260730/
engine       e1ca3b0b224541ac1a3a6c4475d1d07378fa905b57a642cefe5a09b6704da346
audit.json   05cb1698bca3a1237404127bf2c74b0fbc6b9d4931d4aac22327d0254a460f17
~~~

No candidate word was emitted.

## 7. Exact boundary

The catalogue theorem is exhaustive for low-collateral nonprovider
\(E\)-reserve donors in the authenticated H2 source. It is not a theorem
about every arbitrary low-collateral post-service provider across all eight
service ledgers.

The result does not decide:

1. the quarantined \(p0\) H1/four-portal branch;
2. the two donor rows inside \(R19\), where donor and return ownership
   overlap;
3. donors with two or more collateral holes;
4. a return cell outside \(R19\);
5. three or more return edits; or
6. a global rethread outside this fixed chronology.

Accordingly the global bracket remains

\[
12873\le\nu(16)\le12874.
\]
