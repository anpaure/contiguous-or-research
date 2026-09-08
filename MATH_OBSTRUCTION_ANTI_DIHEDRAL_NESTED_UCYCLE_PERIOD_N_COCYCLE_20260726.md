# Anti-dihedral nested Ucycles collapse to wreaths

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or external
input is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad W=\binom{n}{m}.
\tag{0.1}
\]

The proposed anti-dihedral nested-Ucycle gate has an exact obstruction,
already before the Gaussian lower-window conditions are imposed.

Let \(C,D\) be cyclic sliding-window components, with symbol words
\(s=(s_i)_{i\in\mathbb Z_\ell}\) and
\(t=(t_i)_{i\in\mathbb Z_\ell}\), and put

\[
 X_i^s=\{s_i,\ldots,s_{i+m-1}\},\qquad
 Y_j^t=\{t_j,\ldots,t_{j+m}\}.
\tag{0.2}
\]

Assume that the \(m\)-windows on each component are distinct \(m\)-sets
and that a rank-reversing coordinate anti-automorphism

\[
 \theta(A)=[n]\setminus R(A)
\tag{0.3}
\]

maps the first component anti-dihedrally to the second:

\[
 \theta(X_i^s)=Y_{\epsilon i+c}^t,
 \qquad \epsilon\in\{+1,-1\}.
\tag{0.4}
\]

Then

\[
 \boxed{t_{j+n}=t_j\quad(j\in\mathbb Z_\ell).}
\tag{0.5}
\]

Since the \(m\)-windows of \(t\) are distinct, (0.5) forces

\[
 \boxed{\ell=n.}
\tag{0.6}
\]

Moreover one period of \(t\) is a permutation of \([n]\).  Thus every
anti-dihedral sliding-window component is an ordinary length-\(n\) wreath.
This holds whether \(\theta\) fixes a component or pairs two components.

Consequently:

1. for every \(m\ge2\), there is no cyclic word of length \(W\) whose
   \(m\)-windows enumerate \(\binom{[n]}m\) and whose induced
   Middle-Levels cycle is anti-dihedral;
2. every anti-dihedral sliding-window factor has exactly

   \[
                     \boxed{W/n=\operatorname {Cat}_m}
   \tag{0.7}
   \]

   components;
3. the anti-dihedral hypothesis cannot coexist with the required
   \(o(W/m)\)-component fusion; and
4. adding prefix universality at the lengths
   \(m-1,\ldots,m-H\) cannot repair the obstruction, because the collapse
   occurs before any lower coverage constraint is used.

In the two-rotor normal form, let

\[
 A(x_1,\ldots,x_n)=(x_2,\ldots,x_{n-1},x_1,x_n),
\tag{0.8}
\]

\[
 B(x_1,\ldots,x_n)=(x_2,\ldots,x_n,x_1).
\tag{0.9}
\]

The same obstruction says more sharply that anti-dihedral factorhood
forces every selected arc to be a \(B\)-arc.  The \(A\)-arc is the
nonlinear tail switch; it is precisely the freedom needed to fuse wreaths.
Thus anti-dihedral symmetry kills the nonlinear rotor degree of freedom
statewise:

\[
                         \boxed{x_\pi^A=0.}
\tag{0.10}
\]

The rotor circulation then decomposes into pure \(B\)-orbits of length
\(n\).  This is the exact flow/cocycle obstruction requested in the new
lane.  More precisely, the **integral** symmetry face of the rotor
circulation is the wreath face.  Fractional weights on different wreath
orbits may still have an owner-cover integrality gap, but they cannot be
spliced into a longer integral component while (0.4) is retained.

This does not obstruct coefficient one in general.  It proves that exact
componentwise anti-dihedral symmetry is too rigid.  A surviving rotor route
must replace (0.4) by an aggregate lower/upper trace resolution, or allow a
symmetry which is recovered only after combining components and is not an
automorphism of each sliding-window transition cycle.

## 1. Minimal sliding-window facts

Let \(u=(u_i)_{i\in\mathbb Z_\ell}\) be a cyclic symbol word such that its
\(m\)-windows

\[
 Z_i=\{u_i,u_{i+1},\ldots,u_{i+m-1}\}
\tag{1.1}
\]

are distinct \(m\)-sets and consecutive windows are joined by the sliding
update.

### Lemma 1.1 (the \((m+1)\)-windows are injective)

Every \((m+1)\)-term symbol window of \(u\) has distinct entries.

#### Proof

The overlap \(u_{i+1},\ldots,u_{i+m-1}\) already has \(m-1\) distinct
entries.  If the new symbol \(u_{i+m}\) repeated one of them, then
\(Z_{i+1}\) would have fewer than \(m\) members.  If
\(u_{i+m}=u_i\), then \(Z_{i+1}=Z_i\), contrary to distinctness.
\(\square\)

Hence

\[
 Y_i:=Z_i\cup Z_{i+1}
     =\{u_i,u_{i+1},\ldots,u_{i+m}\}
\tag{1.2}
\]

has rank \(m+1\).

### Lemma 1.2 (anti-dihedral symmetry forces \((m+2)\)-injectivity)

Under (0.4), every \((m+2)\)-term window of the target word \(t\) has
distinct entries.

#### Proof

The consecutive lower intersection

\[
 X_i^s\cap X_{i+1}^s
 =\{s_{i+1},\ldots,s_{i+m-1}\}
\tag{1.3}
\]

has rank \(m-1\), by Lemma 1.1.  Applying \(\theta\), and using the two
consecutive instances of (0.4), gives the union of two adjacent
\((m+1)\)-vertices on the target component.  This is the union of three
consecutive \(m\)-windows, hence the set of the \((m+2)\) consecutive
symbols of \(t\).  Rank reversal gives it rank

\[
                         n-(m-1)=m+2.
\]

Therefore those \(m+2\) symbols are distinct.  The phase map in (0.4) is
a bijection, so this holds at every target start. \(\square\)

Lemma 1.2 is the only residence fact needed in the obstruction.  No
Gaussian depth, lower coverage, or PBBS property is used.

## 2. The exact symbol cocycle

For a sliding word \(s\),

\[
 X_{i+1}^s=X_i^s-\{s_i\}+\{s_{i+m}\}.
\tag{2.1}
\]

Applying (0.3) reverses this exchange:

\[
 \theta(X_{i+1}^s)
 =\theta(X_i^s)-\{R(s_{i+m})\}+\{R(s_i)\}.
\tag{2.2}
\]

Lemma 1.2 makes the corresponding exchange of target upper windows
unique.

### Theorem 2.1 (period-\(n\) cocycle)

Under (0.2)--(0.4), the target word satisfies (0.5), for both dihedral
signs.

#### Proof: rotational sign

Suppose \(\epsilon=+1\), and put \(j=i+c\).  Consecutive target upper
windows obey

\[
 Y_{j+1}^t=Y_j^t-\{t_j\}+\{t_{j+m+1}\}.
\tag{2.3}
\]

Equations (0.4), (2.2), and uniqueness of the exchange in (2.3) give

\[
 t_{i+c}=R(s_{i+m}),
 \qquad
 t_{i+c+m+1}=R(s_i).
\tag{2.4}
\]

Replace \(i\) by \(i-m\) in the first identity.  Then

\[
 t_{i-m+c}=R(s_i)=t_{i+c+m+1}.
\tag{2.5}
\]

The two target indices in (2.5) differ by

\[
                         2m+1=n.
\]

As \(i\) ranges cyclically, (0.5) follows.

#### Proof: reflection sign

Suppose \(\epsilon=-1\), and put \(j=-i+c\).  Now increasing the source
index decreases the target index, and

\[
 Y_{j-1}^t=Y_j^t-\{t_{j+m}\}+\{t_{j-1}\}.
\tag{2.6}
\]

Equations (0.4), (2.2), and uniqueness give

\[
 t_{j+m}=R(s_{i+m}),
 \qquad
 t_{j-1}=R(s_i).
\tag{2.7}
\]

Apply the first identity in (2.7) with source index \(i-m\).  Its target
phase is \(j+m\), and hence

\[
 t_{j+2m}=R(s_i)=t_{j-1}.
\tag{2.8}
\]

Again the indices differ by \(2m+1=n\), proving (0.5). \(\square\)

Equation (0.5) is the exact anti-dihedral cocycle.  It is stronger than a
parity or point-margin invariant: it identifies the physical symbol at
every pair of positions separated by \(n\).

## 3. Classification of every component

### Theorem 3.1 (anti-dihedral sliding components are wreaths)

Every component satisfying (0.2)--(0.4) has length \(n\), and one period
of its symbol word is a permutation of \([n]\).

#### Proof

By Theorem 2.1, the target word has period dividing

\[
                         d=\gcd(\ell,n).
\tag{3.1}
\]

If \(d<\ell\), then its \(m\)-windows repeat after \(d\) starts, contrary
to the component's distinct-owner hypothesis.  Hence \(d=\ell\), so

\[
                         \ell\mid n.
\tag{3.2}
\]

An injective \(m\)-window in a cyclic word requires its fundamental period
to be at least \(m+1\).  Since \(n=2m+1\) is odd, every proper divisor of
\(n\) is at most \(n/3<m+1\).  Equation (3.2) therefore forces
\(\ell=n\).

Finally, Lemma 1.1 makes every \((m+1)\)-term window injective.  If two
positions in one length-\(n\) period carried the same coordinate, their
shorter cyclic distance would be at most

\[
                         \lfloor n/2\rfloor=m.
\]

The two occurrences would then lie together in an \((m+1)\)-term window,
a contradiction.  Hence the period contains \(n\) different coordinates
and is a permutation of \([n]\). \(\square\)

### Corollary 3.2 (Hamilton obstruction)

For \(m\ge2\), no length-\(W\) anti-dihedral nested Ucycle exists.

#### Proof

Theorem 3.1 forces its sole component to have length \(n\), whereas

\[
                         \binom{2m+1}{m}>2m+1
\]

for every \(m\ge2\). \(\square\)

### Corollary 3.3 (factor classification)

Every anti-dihedral sliding-window factor which enumerates the middle
layer has exactly \(W/n\) length-\(n\) components.  These are precisely
ordinary cyclic-interval wreaths.

#### Proof

The rank-reversing automorphism permutes the factor components.  Apply
Theorem 3.1 to every component and its image component.  The components
partition \(W\) middle owners, so their number is \(W/n\).  A length-\(n\)
permutation word has middle windows equal to the cyclic \(m\)-intervals of
that permutation, which is exactly a wreath.  Conversely every wreath has
the plain-complement rotational symmetry

\[
                         X_i^c=Y_{i+m}.
\]

Thus the classification is exact. \(\square\)

The component pairing case contains no loophole.  Theorem 2.1 proves
period \(n\) in the **target** component using only the source-to-target
relation (0.4); it does not assume that \(C=D\), that \(R\) is an
involution, or that \(\theta\) fixes a component.

## 4. Collapse of the two-rotor circulation

For a permutation state

\[
                         \pi=(x_1,\ldots,x_n),
\]

the two rotor moves (0.8)--(0.9) induce the same middle-owner transition

\[
 \{x_1,\ldots,x_m\}\longmapsto
 \{x_2,\ldots,x_{m+1}\}.
\tag{4.1}
\]

They differ only in the tail controller.  The \(A\)-move emits
\(x_1\) again after \(n-1\) symbol positions; the \(B\)-move emits the
currently missing symbol and rotates all \(n\) positions.

### Proposition 4.1 (anti-dihedral symmetry kills the tail switch)

On every anti-dihedral sliding component, the rotor control word is
identically \(B\).

#### Proof

By Theorem 3.1 the emitted symbol word is a repeated permutation of
\([n]\).  At state

\[
 \pi_i=(s_i,s_{i+1},\ldots,s_{i+n-2},u_i),
\]

the missing coordinate is

\[
                         u_i=s_{i+n-1}.
\]

Thus the next appended symbol is the missing coordinate, which is exactly
the \(B\)-transition in (0.9). \(\square\)

The exact colored-circulation formulation makes the relation to the rotor
lane explicit.  Let \(x_\pi^A,x_\pi^B\in\{0,1\}\).  With

\[
 \mathcal F_X={\pi:\{\pi_1,\ldots,\pi_m\}=X\},
\tag{4.2}
\]

the owner-transversal and state-conservation equations are

\[
 \sum_{\pi\in\mathcal F_X}(x_\pi^A+x_\pi^B)=1
 \qquad\left(X\in\binom{[n]}m\right),
\tag{4.3}
\]

\[
 x_\rho^A+x_\rho^B
 =x_{A^{-1}\rho}^A+x_{B^{-1}\rho}^B
 \qquad(\rho\in S_n).
\tag{4.4}
\]

The nested lower-cover constraints at depth \(q\) are

\[
 \sum_{\substack{\pi:\{
       \pi_1,\ldots,\pi_{m-q}\}=T}}
       (x_\pi^A+x_\pi^B)\ge1
 \qquad\left(T\in\binom{[n]}{m-q}\right).
\tag{4.5}

Without symmetry, (4.3)--(4.5) are a genuine colored rotor circulation;
the binary \(A/B\) choice is the nonlinear controller.  Proposition 4.1
adds the exact statewise equation

\[
                         x_\pi^A=0.
\tag{4.6}
\]

Equation (4.4) then becomes

\[
                         x_\rho^B=x_{B^{-1}\rho}^B.
\tag{4.7}
\]

Hence the support is a union of complete \(B\)-orbits.  Each selected
orbit has length \(n\) and projects to one wreath.  Equation (4.3) selects
exactly \(W/n\) such orbits.

This is stronger than the usual rotor parity cocycle.  Since
\(A\) is odd and \(B\) is even as a permutation of positions, closure of a
general rotor cycle only forces an even number of \(A\)-moves.  The
anti-dihedral symbol cocycle forces their number to be zero.

## 5. Consequences for Gaussian prefix coverage

The lower-window requirements do not enter Theorems 2.1--3.1.  They now
reduce to the following strictly older problem: choose an exact wreath
factor whose cyclic intervals of lengths

\[
                         m,m-1,\ldots,m-H
\tag{5.1}
\]

cover the corresponding layers.  Even if such a factor exists, exact
anti-dihedral symmetry gives no component reduction.

The componentwise singleton literalization from the proposed gate has
length

\[
 W+{W\over n}(m+H).
\tag{5.2}
\]

For every fixed Gaussian \(H=A\sqrt m\),

\[
 {1\over W}\left[W+{W\over n}(m+H)\right]
 =1+{m+H\over2m+1}
 ={3\over2}+o(1).
\tag{5.3}
\]

Equation (5.3) is the exact cost of the componentwise linearization, not a
universal lower bound for every possible cross-component literal splice.
It is enough to show that the anti-dihedral factor theorem, after the
period collapse, no longer implies coefficient one.

There is also no Hamilton workaround: Corollary 3.2 rules out the single
length-\(W\) cyclic singleton word itself.  Thus lower prefix universality,
however strong, cannot restore the requested object.

## 6. Relation to the earlier rotor-circulation obstruction

The symmetrized rotor master has zero fractional circulation defect, but a
low-switch integral resolution requires one color whose selected state
table has a small directed path cover.  The two-rotor Ucycle lift was a
candidate way to make that color one long orbit: both \(A\) and \(B\)
project to the same Johnson edge, so tail switches appeared able to alter
future prefix flags without disturbing middle ownership.

Theorem 2.1 shows why exact anti-dihedral symmetry cannot be used to close
the upper half of that construction.  Commuting rank reversal with one
projected Johnson step gives the displacement cocycle

\[
                         s_{i+n}=s_i.
\tag{6.1}
\]

In rotor language, (6.1) deletes every \(A\)-arc and leaves only the
length-\(n\) \(B\)-circulation.  Therefore the path-cover number is exactly

\[
                         {W\over n},
\tag{6.2}
\]

not \(o(W/m)\).  Orbit symmetrization, Euler splicing of equal state
occurrences, and fractional mixing cannot change (6.2) while the exact
anti-dihedral relation is retained, because (4.6) holds on every integral
component before any averaging.

The correct redirect is consequently one of the following.

1. Keep the nonlinear two-rotor circulation, including \(A\)-arcs, and
   solve lower and upper prefix coverage jointly rather than deriving the
   upper half from an exact cycle automorphism.
2. Require only aggregate equality of the lower and upper trace-load
   vectors under a coordinate anti-automorphism.  Such an equality need not
   match phases by \(i\mapsto\pm i+c\), so Theorem 2.1 does not apply.
3. Use anti-dihedral wreaths only as local atoms, but let the global splice
   break their componentwise symmetry and repair the upper columns by a
   separate balanced flow.

The first alternative is the closest continuation of the rotor lane.  Its
exact finite problem is (4.3)--(4.5), together with the analogous upper
prefix constraints, but **without** (4.6).  The remaining integrality gap is
then genuine; under exact anti-dihedral symmetry it had collapsed to the
wreath face.

## 7. Logical boundary

The proved obstruction is

\[
 \boxed{
 \begin{gathered}
 \text{sliding middle-window component}\\
 +\ \text{rank-reversing dihedral phase symmetry}
 \end{gathered}
 \Longrightarrow
 \text{one length-}n\text{ wreath}.}
\tag{7.1}
\]

It applies to fixed components and to components paired by the symmetry,
to rotational and reflection signs, and to arbitrary coordinate
permutations \(R\).  It uses only depth one and therefore applies a
fortiori at every fixed Gaussian depth.

It does not say that central nested Ucycles without anti-dihedral symmetry
are impossible.  Nor does it rule out aggregate complement-equivariant
load balancing.  It proves exactly that the proposed method of obtaining
all upper windows for free from a phase-affine rank-reversing automorphism
eliminates the tail-switch freedom needed to build a long rotor orbit.
