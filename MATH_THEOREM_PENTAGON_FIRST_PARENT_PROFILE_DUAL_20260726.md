# Rooted-pentagon profiles at the first parent scale

Date: 2026-07-26

Method: pure mathematics only.

> **Correction (2026-07-26).**  The conclusion of this note is retracted.
> Lemma 2.1 was applied with a false premise: for a general complete
> port-factor substitution, the three cyclic starts complementary to the
> displayed \(2r=6\) parent starts need not remain fixed.  Exactness fixes
> the sum of the two subhistograms, not either subhistogram separately.
> The explicit factor in
> `MATH_THEOREM_D4_PAIR23_PORT_FACTOR_20260726.md` gives
> \(u^+-u^-=2e_2-3e_3-3e_6+4e_7\ne0\) on the six starts and the opposite
> vector on the other three.  The corrected audit is
> `MATH_AUDIT_D4_PAIR23_FULL_PARENT_PROFILE_20260726.md`.  The explicit
> canonical computations in Sections 1, 3, and 4 below remain useful; the
> asserted library-wide equality \(u_G=u_{G_0}\), the residual conclusions,
> and the claimed collar cancellation do not.

## 0. Conclusion

The rooted pentagon itself has semilength three.  Its first one-node
common-context lifts

\[
                    x\longmapsto x10,\qquad
                    x\longmapsto10x,\qquad
                    x\longmapsto1x0
\tag{0.1}
\]

are port-transversal factors of semilength four.  Thus the first genuine
parent test for the lifted library is a size-four parent servicing depth
three.

At that scale the full affected-window histogram is independent of the
chosen library member.  With the local coordinates labelled
\(1,\ldots,8\) and the closing coordinate labelled \(9=\infty\), it is

\[
 \boxed{
 u_G=9e_1+9e_2+12e_3+12e_4+12e_5+12e_6+9e_7+9e_8
 \qquad(G\in\mathscr L_4).}
\tag{0.2}
\]

There is no \(e_9\)-term.  In particular

\[
                         E_\beta(G)=E_\beta(G_0)
                         \qquad(G\in\mathscr L_4),
\tag{0.3}
\]

for every residual background \(\beta\).  Hence no rooted pentagon, no
one-node common-context lift, and no composition of such lifts inside this
one parent has any cap descent at the first parent scale.  The nonzero
intrinsic target directions are exactly repaid by the crossing collars.

The weighted residual-capacity dual therefore degenerates to one fixed
profile.  If \(c_x=(9-\beta_x)_+\), condition (5.8) of the residual-capacity
note is

\[
 \boxed{
  \langle\alpha,u_*\rangle
       \le \langle\alpha,c\rangle+\varepsilon
       \quad(0\le\alpha\le1),}
\tag{0.4}
\]

where \(u_*\) is (0.2).  Equivalently,

\[
 \boxed{
 E^{\rm frac}_\beta(\mathscr L_4)
 =\min_{G\in\mathscr L_4}E_\beta(G)
 =\sum_{x=1}^8(u_*(x)-c_x)_+.}
\tag{0.5}
\]

In the isolated nine-coordinate instance, the unaffected histogram and
the true residual capacities are

\[
\begin{aligned}
 \beta_*&=5e_1+5e_2+2e_3+2e_4+2e_5+2e_6
               +5e_7+5e_8+14e_9,\\
 c_*&=4e_1+4e_2+7e_3+7e_4+7e_5+7e_6+4e_7+4e_8.
\end{aligned}
\tag{0.6}
\]

Therefore the exact value of both sides of the fractional/integral
optimization is

\[
 \boxed{E^{\rm frac}_{\beta_*}(\mathscr L_4)
       =\min_GE_{\beta_*}(G)=40.}
\tag{0.7}
\]

Thus the first parent library is not a cap absorber.  It relocates marked
and offset-resolved occurrences, but its complete affected histogram is
fixed.

The singleton argument is special to this first matched scale.  After an
additional outer lift the protected targets have size greater than one;
point-margin conservation no longer determines their full histogram.
One must then compute the carrier-resolved collars anew.  Formula (0.2)
must not be exported to that larger setting.

## 1. A matched-scale window lemma

Let a rooted size-\(s\) geodesic have deletion and insertion orders

\[
 a_1,\ldots,a_s,qquad b_1,\ldots,b_s,
\]

so that

\[
 X_t=(P\setminus\{a_1,\ldots,a_t\})
       \cup\{b_1,\ldots,b_t\},\qquad0\le t\le s.
\tag{1.1}
\]

The associated local wreath has cyclic lower-state order obtained from

\[
        (a_1,\ldots,a_s,b_1,\ldots,b_s,\infty).
\tag{1.2}
\]

At depth \(r=s-1\), the starts meeting an open parent state are

\[
                         2-s,3-s,\ldots,s-1.
\tag{1.3}
\]

In the canonical member their singleton targets are, in order,

\[
                  a_2,a_3,\ldots,a_s,
                  b_1,b_2,\ldots,b_{s-1}.
\tag{1.4}
\]

Consequently, if \(A_1(x)\) is the number of rooted rows whose first
deletion is \(x\), and \(B_s(x)\) is the number whose last insertion is
\(x\), then the canonical affected histogram is

\[
 \boxed{
              u_0(x)=\operatorname {Cat}_s-A_1(x)-B_s(x),
              \qquad u_0(\infty)=0.}
\tag{1.5}
\]

### Proof

Sliding an \(s\)-window around (1.2) gives the consecutive lower states of
the wreath.  The intersection of \(s\) consecutive \(s\)-windows is the
unique coordinate common to them.  For the starts in (1.3), these common
coordinates are precisely the entries in positions \(2,\ldots,2s-1\) of
(1.2), which proves (1.4).  Each row contains every core coordinate once
in (1.2).  Omitting \(a_1,b_s,\infty\) gives (1.5). \(\square\)

Formula (1.5) computes the old histogram.  It is not legitimate to use an
alternative factor's own cyclic completion to compute its substituted
histogram: in a context substitution the ambient collars, rather than the
alternative local completion, are held fixed.  The next lemma supplies the
correct comparison.

## 2. Singleton rigidity of a full affected histogram

### Lemma 2.1

Let two exact middle factors differ only in a prescribed collection of
affected slots, and suppose the protected targets are singletons.  If
\(u,u'\) are the histograms contributed by those slots, then

\[
                              u'=u.
\tag{2.1}
\]

### Proof

For every exact factor of semilength \(m\), every coordinate belongs to
exactly

\[
                         \operatorname {Cat}_m
\tag{2.2}
\]

rooted depth-\((m-1)\) occurrences.  This is the point-margin identity

\[
              \sum_{S\ni x}\mu_{m-1}(S)=\operatorname {Cat}_m,
\tag{2.3}
\]

and there is only one singleton \(S\) containing \(x\), namely \(\{x\}\).
Thus the complete singleton histogram is the same in the two exact
factors.  All slots outside the prescribed affected collection are fixed,
so subtracting their common histogram proves (2.1). \(\square\)

This is stronger than preservation of a sorted multiplicity profile.  It
fixes every labelled coordinate of \(u\).

## 3. The semilength-three seed

For reference, write the old rooted pentagon paths as

\[
\begin{array}{c|cccc}
1&123&136&146&456\\
2&124&126&156&356\\
3&125&145&345&346\\
4&135&235&245&246\\
5&134&234&236&256.
\end{array}
\tag{3.1}
\]

For a row with flip order

\[
                    (b_1,a_1,b_2,a_2,b_3,a_3),
\]

the four affected starts have the canonical targets

\((a_2,a_3,b_1,b_2)\).  Reading these from (3.1) gives

\[
\begin{array}{c|c}
1&(3,1,6,4)\\
2&(2,1,6,5)\\
3&(1,5,4,3)\\
4&(3,5,2,4)\\
5&(4,3,2,6).
\end{array}
\tag{3.2}
\]

Hence

\[
 \boxed{u^{(3)}_0=3e_1+3e_2+4e_3+4e_4+3e_5+3e_6,}
\tag{3.3}
\]

with zero mass at \(\infty=7\).  Lemma 2.1 implies that every rooted
pentagon factor installed in this same parent has exactly (3.3) as its
full affected histogram.

This makes the collar repayment visible.  The two intrinsic starts have
old histograms

\[
 q^-_0=2e_1+e_3+2e_5,qquad
 q^+_0=2e_2+e_4+2e_6,
\tag{3.4}
\]

and new histograms

\[
 q^-_1=2e_1+e_2+2e_4,qquad
 q^+_1=2e_3+e_5+2e_6.
\tag{3.5}
\]

Therefore

\[
 (q^-_1+q^+_1)-(q^-_0+q^+_0)
                         =e_3+e_4-e_2-e_5.
\tag{3.6}
\]

The two crossing starts have the opposite aggregate direction

\[
                         e_2+e_5-e_3-e_4.
\tag{3.7}
\]

Equations (3.6)--(3.7) cancel exactly.  Thus the familiar intrinsic vector
\(2e_3+e_5-e_4-2e_2\) is a real sector effect, but it is not the full
parent effect.

## 4. The first one-node parent: semilength four

The MSW flip-position recursion is

\[
 \rho(1u0v)=
 \bigl(|u|+2,\ |u|+2-\rho(\operatorname {rev}u),\ 1,
                    |u|+2+\rho(v)\bigr).
\tag{4.1}
\]

If

\[
             \rho(P)=(b_1,a_1,b_2,a_2,b_3,a_3,b_4,a_4),
\]

only \(a_1\) and \(b_4\) are omitted from the six canonical affected
targets.  Applying (4.1) to the fourteen Dyck roots gives

\[
\begin{array}{c|cc@{\qquad}c|cc}
P&a_1&b_4&P&a_1&b_4\\ \hline
1234&2&7&1256&2&7\\
1235&2&7&1257&2&8\\
1236&6&5&1345&1&7\\
1237&2&8&1346&1&5\\
1245&4&3&1347&1&8\\
1246&6&3&1356&1&7\\
1247&4&8&1357&1&8.
\end{array}
\tag{4.2}
\]

Thus

\[
 A_1=5e_1+5e_2+2e_4+2e_6,
 \qquad
 B_4=2e_3+2e_5+5e_7+5e_8.
\tag{4.3}
\]

Substitution in (1.5), using \(\operatorname {Cat}_4=14\), yields

\[
 \boxed{
 u^{(4)}_0
 =9e_1+9e_2+12e_3+12e_4+12e_5+12e_6+9e_7+9e_8.}
\tag{4.4}
\]

Its total mass is

\[
                  4\cdot9+4\cdot12=84
                  =2(3)\operatorname {Cat}_4,
\]

as required.

Every factor obtained from the rooted pentagon by one of (0.1) is an exact
port-transversal size-four substitute.  Any legal composition of such
packet switches is again exact and changes only the prescribed parent
slots.  Lemma 2.1 therefore gives

\[
                         u_G=u^{(4)}_0
                         \qquad(G\in\mathscr L_4),
\tag{4.5}
\]

which proves (0.2).

For example, in the right lift \(x10\), the distinguished intrinsic start
has the signed direction

\[
                         2e_3+e_5-e_4-2e_2.
\tag{4.6}
\]

Equation (4.5) forces the sum of the remaining affected offsets to have
the negative of (4.6).  The same statement holds, after the appropriate
coordinate embedding, for \(10x\) and \(1x0\).  Consequently it is
incorrect to multiply the intrinsic negative mass by the number of
parent packets and credit it as cap drain.

## 5. Exact test of the weighted residual-capacity dual

Let \(c=c_\beta\) be any residual-capacity vector on the singleton targets.
Since the library has the common profile \(u_*\), its fractional defect is

\[
\begin{aligned}
 E^{\rm frac}_\beta(\mathscr L_4)
 &=\min_{\nu}\sum_x
       \left(\sum_G\nu(G)u_G(x)-c_x\right)_+\\
 &=\sum_x(u_*(x)-c_x)_+.
\end{aligned}
\tag{5.1}
\]

There is no integral gap:

\[
 \operatorname {IG}_\beta(\mathscr L_4)=0,
\tag{5.2}
\]

but only because randomization and integral choice produce the same
histogram.  This is rigidity, not useful rounding.

The dual identity

\[
 \max_{0\le\alpha\le1}\langle\alpha,u_*-c\rangle
                  =\sum_x(u_*(x)-c_x)_+
\tag{5.3}
\]

shows that (5.8) holds with error \(\varepsilon\) exactly when the right
side of (5.3) is at most \(\varepsilon\).  In particular, zero fractional
defect is equivalent to

\[
\begin{array}{c}
 c_1,c_2,c_7,c_8\ge9,\\
 c_3,c_4,c_5,c_6\ge12.
\end{array}
\tag{5.4}

At local semilength four the cap is \(p=9\), so the second line is
impossible even before the true unaffected load is inserted.  The smaller
capacity-only witness

\[
                         \alpha=1_{\{3,4,5,6\}}
\tag{5.5}
\]

gives

\[
 \min_{G\in\mathscr L_4}\langle\alpha,u_G\rangle=48,
 \qquad
 \langle\alpha,c_\beta\rangle\le36.
\tag{5.6}
\]

This forces \(\varepsilon\ge12\) for every possible residual background.

For the actual isolated parent, the full exact factor has singleton
histogram \(14\sum_{x=1}^9e_x\).  Subtracting (4.4) gives

\[
 \beta_*=5e_1+5e_2+2e_3+2e_4+2e_5+2e_6
               +5e_7+5e_8+14e_9,
\tag{5.7}
\]

and hence

\[
 c_*=4e_1+4e_2+7e_3+7e_4+7e_5+7e_6+4e_7+4e_8.
\tag{5.8}
\]

Every one of the eight core coordinates contributes exactly five units
to the residual defect.  Thus

\[
 E^{\rm frac}_{\beta_*}(\mathscr L_4)
 =\min_GE_{\beta_*}(G)=8\cdot5=40,
\tag{5.9}
\]

with dual maximizer \(\alpha=1_{[8]}\).  This proves (0.7).  More
importantly for descent, for every \(G\)

\[
 E_\beta(G)-E_\beta(G_0)=0.
\tag{5.10}
\]

Thus the library has no state, no weight, and no residual-capacity vector
at this scale on which it strictly improves the old parent.  All apparent
improvements obtained from only one intrinsic child map omit an equal
collar repayment.

## 6. Exact scope of the obstruction

Lemma 2.1 uses that depth \(m-1\) targets are singletons.  For an additional
outer common context, the same local size-four packet may act on targets
of the form

\[
                             B\cup R,
\]

where \(B\) is an exterior carrier and \(|R|\) need not be one uniformly
over the crossing offsets.  Point conservation then says only

\[
                 \sum_{S\ni x}(u_G-u_{G_0})(S)=0,
\]

and carrier conservation says only

\[
                 \sum_{S:S\setminus J=B}(u_G-u_{G_0})(S)=0.
\]

Neither identity forces \(u_G=u_{G_0}\) when targets have size greater
than one.  Therefore the present theorem is a complete negative answer at
the first parent scale, not a no-go for all higher lifts.  A higher-scale
positive claim must display the actual carrier-resolved crossing tables
and verify (5.8) against their true residual capacities.  Intrinsic
pentagon histograms alone cannot do so.
